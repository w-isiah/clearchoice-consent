from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

# Validate env
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ SUPABASE_URL and SUPABASE_KEY must be set in .env")

if not SUPABASE_URL.startswith("https://") or ".supabase.co" not in SUPABASE_URL:
    raise ValueError(f"❌ Invalid Supabase URL format: {SUPABASE_URL}")

# Single shared client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_user_action(
    user_id: str,
    action: str,
    model: str | None = None,
    tokens_used: int = 0,
    success: bool = True,
):
    """Insert one row into user_history."""
    if not user_id or not action:
        return
    try:
        supabase.table("user_history").insert({
            "user_id": user_id,
            "action": action,
            "model": model,
            "tokens_used": tokens_used,
            "success": success,
        }).execute()
    except Exception as e:
        print(f"⚠️ Failed to log user action: {e}")

def get_user_history(user_id: str):
    """Return history newest first."""
    resp = (
        supabase.table("user_history")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return resp.data or []

def clear_user_history(user_id: str):
    """Delete a user's history."""
    return supabase.table("user_history").delete().eq("user_id", user_id).execute()
