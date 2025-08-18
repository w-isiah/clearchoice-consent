from fastapi import APIRouter
from pydantic import BaseModel

# 1. Define the router
router = APIRouter()

# 2. Request body model
class ChatRequest(BaseModel):
    question: str

# 3. Route
@router.post("/")
def chat_advisor(request: ChatRequest):
    # Placeholder logic, can replace with GPT-5 integration later
    answer = f"Advice for your question: {request.question}"
    return {"answer": answer}
