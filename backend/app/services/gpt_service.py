# app/services/gpt_service.py
from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.routes.preferences import supabase  # For logging user actions

# 1. Check API key
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is not set in .env. Please add it before running the app.")

# 2. Initialize OpenAI client (AIML API)
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aimlapi.com/v1",
)

# 3. Logging helper
def log_user_action(user_id: str, action: str, model: str, tokens_used: int = 0, success: bool = True):
    """Logs a user action in Supabase table 'user_history'"""
    try:
        supabase.table("user_history").insert({
            "user_id": user_id,
            "action": action,
            "model": model,
            "tokens_used": tokens_used,
            "success": success
        }).execute()
    except Exception as e:
        print(f"⚠️ Failed to log action: {str(e)}")


# 4. GPT-5 Summarization
def summarize_text(user_id: str, text: str) -> str:
    """Summarizes text using GPT-5 and logs the action"""
    model_name = "gpt-5-chat-latest"
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": f"Summarize this: {text}"}],
            temperature=0.5,
            max_tokens=300,
        )
        summary = response.choices[0].message.content
        tokens = getattr(response.usage, "total_tokens", 0)
        log_user_action(user_id, "summarized text", model=model_name, tokens_used=tokens, success=True)
        return summary
    except Exception as e:
        log_user_action(user_id, "summarize text failed", model=model_name, tokens_used=0, success=False)
        raise e


# 5. GPT-5 Consent Advice
def chat_advice(user_id: str, prompt: str) -> str:
    """Provides advice using GPT-5 and logs the action"""
    model_name = "gpt-5-chat-latest"
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300,
        )
        answer = response.choices[0].message.content
        tokens = getattr(response.usage, "total_tokens", 0)
        log_user_action(user_id, f"asked: {prompt}", model=model_name, tokens_used=tokens, success=True)
        return answer
    except Exception as e:
        log_user_action(user_id, f"ask failed: {prompt}", model=model_name, tokens_used=0, success=False)
        raise e
