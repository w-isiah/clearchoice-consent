from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.services.db_service import log_user_action  # centralized logging

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is not set in .env.")

# AIML API (OpenAI-compatible)
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aimlapi.com/v1",
)

MODEL_NAME = "gpt-5-chat-latest"

def summarize_text(user_id: str, text: str) -> str:
    """Summarize text with GPT-5 and log usage."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": f"Summarize this: {text}"}],
            temperature=0.5,
            max_tokens=300,
        )
        summary = response.choices[0].message.content
        tokens = getattr(response, "usage", None)
        total_tokens = getattr(tokens, "total_tokens", 0) if tokens else 0

        log_user_action(
            user_id=user_id,
            action="summarized text",
            model=MODEL_NAME,
            tokens_used=total_tokens,
            success=True,
        )
        return summary
    except Exception as e:
        log_user_action(
            user_id=user_id,
            action="summarize text failed",
            model=MODEL_NAME,
            tokens_used=0,
            success=False,
        )
        raise e

def chat_advice(user_id: str, prompt: str) -> str:
    """Get consent advice with GPT-5 and log usage."""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        answer = response.choices[0].message.content
        tokens = getattr(response, "usage", None)
        total_tokens = getattr(tokens, "total_tokens", 0) if tokens else 0

        log_user_action(
            user_id=user_id,
            action=f"asked: {prompt}",
            model=MODEL_NAME,
            tokens_used=total_tokens,
            success=True,
        )
        return answer
    except Exception as e:
        log_user_action(
            user_id=user_id,
            action=f"ask failed: {prompt}",
            model=MODEL_NAME,
            tokens_used=0,
            success=False,
        )
        raise e
