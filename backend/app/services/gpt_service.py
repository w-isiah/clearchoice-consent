import os
import openai

openai.api_key = os.getenv("097a9f01a3a640caba71388c25d586ed")

def summarize_text(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    return response.choices[0].message["content"]
