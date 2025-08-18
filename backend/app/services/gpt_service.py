import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


# Read API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client for AIML API
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=api_key,
)

def summarize_text(text: str) -> str:
    """
    Summarizes the given text using GPT-4o via AIML API.
    """
    response = client.chat.completions.create(
        model="gpt-4o",  # AIML API supported model
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
    )
    return response.choices[0].message.content
