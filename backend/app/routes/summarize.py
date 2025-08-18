from fastapi import APIRouter
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
    summary = summarize_text(request.text)
    return {"summary": summary}
