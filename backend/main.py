from fastapi import FastAPI, Request
from db import supabase

app = FastAPI(title="GuardRail Target API")

def log_event(ip, user_agent, fingerprint, status, threat_score):
    data = {
        "ip": ip,
        "user_agent": user_agent,
        "fingerprint": fingerprint,
        "status": status,
        "threat_score": threat_score
    }
    try:
        supabase.table("request_logs").insert(data).execute()
    except Exception as e:
        print("DB insert failed:", e)

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/health")
def health():
    return {"api": "ok", "db": "connected"}

@app.post("/log-test")
async def log_test(request: Request):
    ip = request.client.host
    user_agent = request.headers.get("user-agent")

    log_event(ip, user_agent, "test_fp", "allowed", 5)
    return {"message": "Logged to Supabase"}

# Victim endpoints (Person B will guard these later)
@app.post("/login")
def login():
    return {"status": "login ok"}

@app.post("/transfer")
def transfer():
    return {"status": "transfer ok"}

@app.get("/home")
def home():
    return {"status": "home ok"}

# For Person C (Dashboard)
@app.get("/logs")
def get_logs(limit: int = 20):
    res = supabase.table("request_logs").select("*").order("id", desc=True).limit(limit).execute()
    return res.data