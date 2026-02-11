import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="GuardRail Dashboard",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛡 GuardRail Demo")

if st.sidebar.button("🔄 Refresh"):
    st.rerun()

st.sidebar.markdown("### Simulate Traffic")

if st.sidebar.button("✅ Normal (+1)"):
    requests.post(f"{API}/simulate/normal")
    st.rerun()

if st.sidebar.button("⚡ Rate-Limit (+6)"):
    requests.post(f"{API}/simulate/rate-limit")
    st.rerun()

if st.sidebar.button("🤖 Bot (+12)"):
    requests.post(f"{API}/simulate/bot")
    st.rerun()

if st.sidebar.button("🧹 Clear All"):
    requests.post(f"{API}/admin/clear")
    st.rerun()

# ---------------- FETCH DATA ----------------
status = requests.get(f"{API}/status/login").json()
metrics = requests.get(f"{API}/metrics").json()
logs = pd.DataFrame(requests.get(f"{API}/logs").json())

limit = status["limit"]
reset = status["reset_in"]
blocked_active = status["blocked"]

normal = status["breakdown"]["normal"]
rate = status["breakdown"]["rate_limit"]
bot = status["breakdown"]["bot"]
total_used = status["total_used"]

# ---------------- HEADER ----------------
st.markdown("## 🛡 GuardRail – Login Protection")
st.caption("Explainable rate-limit enforcement for API security")
st.divider()

# ---------------- TOP METRICS ----------------
m1, m2, m3, m4 = st.columns(4)

m1.metric("Total Requests", metrics["total_requests"])
m2.metric("Blocked Requests", metrics["blocked_requests"])
m3.metric("Requests Used", f"{total_used} / {limit}")
m4.metric("Resets In", f"{reset} sec")

st.metric(
    "Blocking Status",
    "ACTIVE ❌" if blocked_active else "SAFE ✅"
)

# ---------------- OVERLOAD BAR ----------------
st.progress(min(total_used / (limit * 2), 1.0))
st.caption("Overload severity • Blocking begins after 15 requests/min")

# ---------------- BREAKDOWN PANEL ----------------
st.subheader("📊 Traffic Breakdown (current window)")

b1, b2, b3 = st.columns(3)

def breakdown_card(label, value):
    if value >= limit:
        state = "🔴"
    elif value >= 10:
        state = "🟠"
    else:
        state = "🟢"
    st.metric(label, f"{value} / {limit}", delta=state)

breakdown_card("Normal Traffic", normal)
breakdown_card("Rate-Limit Traffic", rate)
breakdown_card("Bot Traffic", bot)

# ---------------- BLOCK REASON PANEL ----------------
st.subheader("🧠 GuardRail Decision Explanation")

if blocked_active:
    reasons = []

    if total_used > limit:
        reasons.append("• Login threshold exceeded (15 requests per minute)")

    if rate >= 10:
        reasons.append("• Sustained burst pattern detected (rate-limit behavior)")

    if bot >= 10:
        reasons.append("• High-frequency automated traffic detected (bot pattern)")

    reasons.append("• Automatic protection engaged until window reset")

    st.error("🚫 **Blocking Active**")
    for r in reasons:
        st.markdown(r)

else:
    st.success("✅ **Protection Ready**")
    st.markdown("• Traffic within safe limits")
    st.markdown("• No automated mitigation required")
    st.markdown("• GuardRail monitoring continues")

# ---------------- LOGS ----------------
if not logs.empty:
    logs["created_at"] = pd.to_datetime(logs["created_at"])
    logs["risk_level"] = logs["risk_level"].str.upper()

    st.subheader("🚨 Recent Blocked Requests")
    st.dataframe(
        logs[logs["risk_level"] == "BLOCKED"]
        [["endpoint", "status_code", "created_at"]]
        .head(10),
        use_container_width=True
    )
else:
    st.info("No logs yet")
