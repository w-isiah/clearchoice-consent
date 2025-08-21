from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gpt_service import summarize_text
from app.services.db_service import log_user_action  # use centralized logging

router = APIRouter()

class SummarizeRequest(BaseModel):
    user_id: str
    text: str

@router.post("/")
def summarize(request: SummarizeRequest):
    if not request.user_id.strip() or not request.text.strip():
        raise HTTPException(status_code=400, detail="user_id and text cannot be empty")
    try:
        summary = summarize_text(request.user_id, request.text)
        log_user_action(request.user_id, f"Summarized text: {request.text[:50]}...")
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT-5 API error: {str(e)}")
