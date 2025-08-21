# app/routes/history.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

router = APIRouter()

class HistoryRequest(BaseModel):
    user_id: str

# Initialize Supabase client safely
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Supabase URL and KEY must be set in .env")
if not SUPABASE_URL.startswith("https://") or not SUPABASE_URL.endswith(".supabase.co"):
    raise ValueError(f"❌ Invalid Supabase URL format: {SUPABASE_URL}")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.get("/")
def get_history(user_id: str):
    if not user_id.strip():
        raise HTTPException(status_code=400, detail="user_id cannot be empty")
    
    try:
        response = supabase.table("user_history").select("*").eq("user_id", user_id).order("timestamp", desc=True).execute()
        return {
            "user_id": user_id,
            "history": response.data or []
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")
