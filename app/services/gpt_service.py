# backend/gpt_service.py
from openai import OpenAI
import os
from app.db_service import get_db_connection

# 1. Check API key
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = '2b511a19c2694a3d90a0f86173d4a510'
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is not set in environment variables.")

# 2. Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.aimlapi.com/v1")

# 3. Logging helper
def log_user_action(user_id: str, action: str, model: str, tokens_used: int = 0, success: bool = True):
    """Logs a user action in MySQL table 'user_history'"""
    conn = get_db_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        sql = """
        INSERT INTO user_history (user_id, action, model, tokens_used, success)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (user_id, action, model, tokens_used, success))
        conn.commit()
    except Exception as e:
        print(f"⚠️ Failed to log action: {str(e)}")
    finally:
        cursor.close()
        conn.close()

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
        log_user_action(user_id, "summarized text", model_name, tokens_used=tokens, success=True)
        return summary
    except Exception as e:
        log_user_action(user_id, "summarize failed", model_name, success=False)
        raise e

# 5. GPT-5 Chat Advice
def chat_advice(user_id, history):
    """
    Generate advice based on full conversation history.
    History is a list of dicts: [{role: "user"/"assistant", content: "..."}]
    """
    messages = [{"role": "system", "content": "You are Consent Guardian, a helpful assistant about consent and safety."}]
    messages.extend(history)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500,
    )
    return response.choices[0].message.content

