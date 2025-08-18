from fastapi import APIRouter
from pydantic import BaseModel

# 1. Define the router
router = APIRouter()

# 2. Request body model
class HistoryRequest(BaseModel):
    user_id: str

# 3. Route
@router.get("/")
def get_history(user_id: str):
    # Placeholder: fetch from Supabase or DB later
    return {
        "user_id": user_id,
        "history": [
            {"action": "summarized consent", "timestamp": "2025-08-18T10:00:00Z"},
            {"action": "updated preferences", "timestamp": "2025-08-18T11:00:00Z"}
        ]
    }
