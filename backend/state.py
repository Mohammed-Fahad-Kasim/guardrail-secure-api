# backend/state.py

import random
import time

_metrics = {
    "total_requests": 39,
    "blocked_requests": 24,
    "threat_score": 84,
    "threat_level": "HIGH",
    "reasons": {
        "rate_limit": 39,
        "behavior": 30,
        "fingerprint": 15,
    },
    "events": [
        {"msg": "High request burst detected", "time": "12:01:02"},
        {"msg": "Threat score crossed threshold", "time": "12:01:04"},
        {"msg": "Client blocked automatically", "time": "12:01:05"},
    ],
}

def get_metrics():
    return _metrics

def simulate_bot_attack():
    _metrics["total_requests"] += random.randint(5, 15)
    _metrics["blocked_requests"] += random.randint(2, 6)
    _metrics["threat_score"] = min(100, _metrics["threat_score"] + random.randint(5, 10))

    _metrics["events"].insert(
        0,
        {
            "msg": "Simulated bot attack",
            "time": time.strftime("%H:%M:%S"),
        },
    )
