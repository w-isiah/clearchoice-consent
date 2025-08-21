# app/services/db_service.py
from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

# 1. Initialize Supabase client safely
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Supabase URL and KEY must be set in .env")

if not SUPABASE_URL.startswith("https://") or not SUPABASE_URL.endswith(".supabase.co"):
    raise ValueError(f"❌ Invalid Supabase URL format: {SUPABASE_URL}")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 2. Log user actions in user_history
def log_user_action(user_id: str, action: str):
    if not user_id.strip() or not action.strip():
        return
    try:
        supabase.table("user_history").insert({
            "user_id": user_id,
            "action": action
        }).execute()
    except Exception as e:
        print(f"⚠️ Failed to log user action: {str(e)}")
