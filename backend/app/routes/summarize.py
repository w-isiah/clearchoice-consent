from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gpt_service import summarize_text

router = APIRouter()

class SummarizeRequest(BaseModel):
    user_id: str
    text: str

@router.post("/")
def summarize(req: SummarizeRequest):
    if not req.user_id.strip() or not req.text.strip():
        raise HTTPException(status_code=400, detail="user_id and text cannot be empty")
    try:
        summary = summarize_text(req.user_id, req.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT-5 API error: {str(e)}")
