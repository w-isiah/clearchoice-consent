from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.db_service import supabase

router = APIRouter()

class PreferenceRequest(BaseModel):
    user_id: str
    preference: str

@router.post("/")
def save_preference(req: PreferenceRequest):
    if not req.user_id.strip() or not req.preference.strip():
        raise HTTPException(status_code=400, detail="user_id and preference cannot be empty")
    try:
        resp = (
            supabase.table("user_preferences")
            .upsert({"user_id": req.user_id, "preference": req.preference})
            .execute()
        )
        return {"status": "success", "data": resp.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preference: {str(e)}")
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.db_service import supabase

router = APIRouter()

class PreferenceRequest(BaseModel):
    user_id: str
    preference: str

@router.post("/")
def save_preference(req: PreferenceRequest):
    if not req.user_id.strip() or not req.preference.strip():
        raise HTTPException(status_code=400, detail="user_id and preference cannot be empty")
    try:
        resp = (
            supabase.table("user_preferences")
            .upsert({"user_id": req.user_id, "preference": req.preference})
            .execute()
        )
        return {"status": "success", "data": resp.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preference: {str(e)}")
