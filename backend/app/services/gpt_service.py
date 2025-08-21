from openai import OpenAI
from app.core.config import OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise ValueError(
        "❌ OPENAI_API_KEY is not set in .env. Please add it before running the app."
    )

# Initialize OpenAI client for AIML API
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aimlapi.com/v1",
)

def summarize_text(text: str) -> str:
    """
    Summarizes the given text using GPT-5 via AIML API.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",  # ✅ updated
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        temperature=0.5,
        max_tokens=300,
    )
    return response.choices[0].message.content


def chat_advice(prompt: str) -> str:
    """
    Provides consent advice based on the input prompt using GPT-5.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",  # ✅ updated
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300,
    )
    return response.choices[0].message.content
from openai import OpenAI
from app.core.config import OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise ValueError(
        "❌ OPENAI_API_KEY is not set in .env. Please add it before running the app."
    )

# Initialize OpenAI client for AIML API
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.aimlapi.com/v1",
)

def summarize_text(text: str) -> str:
    """
    Summarizes the given text using GPT-5 via AIML API.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",  # ✅ updated
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        temperature=0.5,
        max_tokens=300,
    )
    return response.choices[0].message.content


def chat_advice(prompt: str) -> str:
    """
    Provides consent advice based on the input prompt using GPT-5.
    """
    response = client.chat.completions.create(
        model="gpt-5-chat-latest",  # ✅ updated
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300,
    )
    return response.choices[0].message.content
