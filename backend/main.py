from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.state import get_metrics, simulate_bot_attack
from backend.db import get_blocked_clients

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/metrics")
def metrics():
    return get_metrics()

@app.get("/api/blocked-clients")
def blocked_clients():
    return get_blocked_clients()

@app.post("/api/simulate/bot")
def simulate_bot():
    simulate_bot_attack()
    return {"status": "ok"}
