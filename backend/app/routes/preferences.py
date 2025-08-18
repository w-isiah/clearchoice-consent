from fastapi import APIRouter
from pydantic import BaseModel

# 1. Define the router
router = APIRouter()

# 2. Request body model
class PreferenceRequest(BaseModel):
    user_id: str
    preference: str

# 3. Route
@router.post("/")
def save_preference(request: PreferenceRequest):
    # Placeholder: save to Supabase or DB later
    return {"status": "success", "user_id": request.user_id, "preference": request.preference}
