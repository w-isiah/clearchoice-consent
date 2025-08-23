from fastapi import APIRouter, HTTPException, Query
from app.services.db_service import get_user_history, clear_user_history

router = APIRouter()

@router.get("/")
def history(user_id: str = Query(..., min_length=1)):
    try:
        data = get_user_history(user_id)
        return {"user_id": user_id, "history": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")

@router.delete("/clear")
def history_clear(user_id: str = Query(..., min_length=1)):
    try:
        clear_user_history(user_id)
        return {"status": "cleared", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing history: {str(e)}")
