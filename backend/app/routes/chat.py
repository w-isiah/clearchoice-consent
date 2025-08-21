# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gpt_service import chat_advice

# 1. Initialize router
router = APIRouter()

# 2. Request body model
class ChatRequest(BaseModel):
    question: str

# 3. Route for GPT-5 powered advice
@router.post("/")
def chat_advisor(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="⚠️ Question cannot be empty")

    try:
        # Call GPT-5 service
        answer = chat_advice(request.question)

        return {
            "status": "success",
            "question": request.question,
            "answer": answer,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"❌ GPT-5 API error: {str(e)}"
        )
