# backend/db.py

import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

# Force-load backend/.env explicitly
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        f"Supabase credentials not found. Checked path: {ENV_PATH}"
    )

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_blocked_clients():
    response = supabase.table("blocked_clients").select("*").execute()
    return response.data
