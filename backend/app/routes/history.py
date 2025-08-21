# app/routes/history.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY
from datetime import datetime

# 1. Initialize router
router = APIRouter()

# 2. Request body model for logging
class HistoryLogRequest(BaseModel):
    user_id: str
    action: str  # e.g., "summarized consent", "updated preferences"

# 3. Initialize Supabase client safely
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Supabase URL and KEY must be set in .env")

if not SUPABASE_URL.startswith("https://") or not SUPABASE_URL.endswith(".supabase.co"):
    raise ValueError(f"❌ Invalid Supabase URL format: {SUPABASE_URL}")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 4. Route to fetch consent history
@router.get("/")
def get_history(user_id: str):
    if not user_id.strip():
        raise HTTPException(status_code=400, detail="⚠️ user_id cannot be empty")

    try:
        response = (
            supabase.table("user_history")
            .select("*")
            .eq("user_id", user_id)
            .order("timestamp", desc=True)
            .execute()
        )
        return {
            "status": "success",
            "user_id": user_id,
            "history": response.data or [],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error fetching history: {str(e)}")


# 5. Route to log a new action
@router.post("/")
def log_action(request: HistoryLogRequest):
    if not request.user_id.strip() or not request.action.strip():
        raise HTTPException(status_code=400, detail="⚠️ user_id and action cannot be empty")

    try:
        response = (
            supabase.table("user_history")
            .insert({
                "user_id": request.user_id,
                "action": request.action,
                "timestamp": datetime.utcnow().isoformat()  # store ISO UTC timestamp
            })
            .execute()
        )

        return {
            "status": "success",
            "message": "Action logged",
            "log": response.data,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error logging action: {str(e)}")
