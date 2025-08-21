from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.db_service import supabase

router = APIRouter()

class HistoryRequest(BaseModel):
    user_id: str

@router.get("/")
def get_history(user_id: str):
    if not user_id.strip():
        raise HTTPException(status_code=400, detail="user_id cannot be empty")
    try:
        response = supabase.table("user_history").select("*").eq("user_id", user_id).order("timestamp", desc=True).execute()
        return {"user_id": user_id, "history": response.data or []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")
