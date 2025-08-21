from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.db_service import supabase, log_user_action

router = APIRouter()

class PreferenceRequest(BaseModel):
    user_id: str
    preference: str

@router.post("/")
def save_preference(request: PreferenceRequest):
    if not request.user_id.strip() or not request.preference.strip():
        raise HTTPException(status_code=400, detail="user_id and preference cannot be empty")
    try:
        response = supabase.table("user_preferences").upsert({
            "user_id": request.user_id,
            "preference": request.preference
        }).execute()
        log_user_action(request.user_id, f"Updated preference: {request.preference}")
        return {"status": "success", "user_id": request.user_id, "preference": request.preference, "supabase_response": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preference: {str(e)}")
