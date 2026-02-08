import streamlit as st
import pandas as pd
import time
import requests

API_URL = "http://127.0.0.1:8000/logs"
COUNT_URL = "http://127.0.0.1:8000/logs/count"
BLOCKED_COUNT_URL = "http://127.0.0.1:8000/logs/blocked/count"
REFRESH_SECONDS = 1

pd.set_option("display.max_colwidth", 30)

st.set_page_config(page_title="Secure API Abuse Detection", layout="wide")

st.markdown("""
# 🛡️ Secure API Abuse & Rate-Limit Bypass Detection  
**Real-time behavioral security monitoring dashboard**
""")
st.caption("Live traffic • Behavioral analysis • Automated blocking")
st.divider()

# Sidebar
st.sidebar.title("⚙️ Dashboard Info")
st.sidebar.markdown("**Environment:** Hackathon Simulation")
st.sidebar.markdown("**Detection Type:** Behavioral Fingerprinting")
st.sidebar.markdown("**Protection:** Active")
st.sidebar.markdown("**Mode:** API")

# Metrics
col1, col2, col3 = st.columns(3)
total_ph = col1.empty()
blocked_ph = col2.empty()
threat_ph = col3.empty()

st.subheader("📈 Traffic Intensity (Requests / Second)")
chart_ph = st.empty()

st.subheader("🚨 Recently Blocked Requests")
table_ph = st.empty()


# ---------- Styling helpers ----------
def decision_style(val):
    return "color:#d32f2f; font-weight:bold" if str(val).upper() == "BLOCKED" else "color:#2e7d32"


# ---------- Main loop ----------
while True:
    try:
        df = pd.DataFrame(requests.get(API_URL, timeout=3).json())
    except Exception as e:
        st.error(f"API error: {e}")
        time.sleep(REFRESH_SECONDS)
        continue

    if df.empty:
        st.info("Waiting for logs...")
        time.sleep(REFRESH_SECONDS)
        continue

    # ---- FIXED COLUMN MAPPING ----
    df["risk_level"] = df["risk_level"].astype(str).str.upper()
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    df = df.sort_values("created_at", ascending=False)

    # Lifetime stats
    total_requests = requests.get(COUNT_URL).json().get("total", 0)
    blocked_requests = requests.get(BLOCKED_COUNT_URL).json().get("blocked_total", 0)

    recent_total = len(df)
    recent_blocked = len(df[df["risk_level"] == "BLOCKED"])

    total_ph.metric("📥 Total Requests (Lifetime)", total_requests)
    blocked_ph.metric(
        "🚫 Blocked Requests (Lifetime)",
        blocked_requests,
        delta=f"{round((recent_blocked/max(recent_total,1))*100,1)}% recent"
    )

    threat = (
        "LOW 🟢" if recent_blocked < 2
        else "MEDIUM 🟠" if recent_blocked < 6
        else "HIGH 🔴"
    )
    threat_ph.metric("Threat Level", threat)

    # RPS chart
    rps_df = df.set_index("created_at").resample("1S").size()
    chart_ph.line_chart(rps_df.tail(30))

    # Blocked table
    blocked_df = (
        df[df["risk_level"] == "BLOCKED"]
        .head(10)
        .rename(columns={
            "endpoint": "Endpoint",
            "method": "Method",
            "risk_level": "Decision",
            "status_code": "HTTP Code"
        })
    )

    table_ph.dataframe(
        blocked_df.style.applymap(decision_style, subset=["Decision"]),
        use_container_width=True
    )

    time.sleep(REFRESH_SECONDS)
