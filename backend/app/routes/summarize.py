# app/routes/summarize.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gpt_service import summarize_text

# 1. Define the router
router = APIRouter()

# 2. Request body model
class SummarizeRequest(BaseModel):
    text: str

# 3. Route
@router.post("/")
def summarize(request: SummarizeRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    try:
        summary = summarize_text(request.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT-5 API error: {str(e)}")
