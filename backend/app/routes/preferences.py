# app/routes/preferences.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

router = APIRouter()

class PreferenceRequest(BaseModel):
    user_id: str
    preference: str

# Initialize Supabase client safely
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Supabase URL and KEY must be set in .env")
if not SUPABASE_URL.startswith("https://") or not SUPABASE_URL.endswith(".supabase.co"):
    raise ValueError(f"❌ Invalid Supabase URL format: {SUPABASE_URL}")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/")
def save_preference(request: PreferenceRequest):
    if not request.user_id.strip() or not request.preference.strip():
        raise HTTPException(status_code=400, detail="user_id and preference cannot be empty")
    
    try:
        response = supabase.table("user_preferences").upsert({
            "user_id": request.user_id,
            "preference": request.preference,
        }).execute()
        # Log action
        supabase.table("user_history").insert({
            "user_id": request.user_id,
            "action": f"Updated preference: {request.preference}"
        }).execute()
        return {
            "status": "success",
            "user_id": request.user_id,
            "preference": request.preference,
            "supabase_response": response.data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preference: {str(e)}")
