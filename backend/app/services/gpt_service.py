# app/services/gpt_service.py
from openai import OpenAI
from app.core.config import OPENAI_API_KEY
from app.services.db_service import log_user_action  # centralized logging

# 1. Validate API key
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is not set in .env. Please add it before running the app.")

# 2. Initialize OpenAI client (AIML API)
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aimlapi.com/v1",
)

# 3. GPT-5 Summarization
def summarize_text(user_id: str, text: str) -> str:
    """
    Summarizes text using GPT-5 and logs the action.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        temperature=0.5,
        max_tokens=300,
    )
    summary = response.choices[0].message.content
    log_user_action(user_id, f"Summarized text: {text[:50]}...")
    return summary

# 4. GPT-5 Consent Advice
def chat_advice(user_id: str, prompt: str) -> str:
    """
    Provides consent advice using GPT-5 and logs the action.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300,
    )
    answer = response.choices[0].message.content
    log_user_action(user_id, f"Asked: {prompt}")
    return answer
