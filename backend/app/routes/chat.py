# app/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gpt_service import chat_advice

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    question: str

@router.post("/")
def chat_advisor(request: ChatRequest):
    if not request.user_id.strip() or not request.question.strip():
        raise HTTPException(status_code=400, detail="user_id and question cannot be empty")
    
    try:
        answer = chat_advice(request.user_id, request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT-5 API error: {str(e)}")
