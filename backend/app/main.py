from fastapi import FastAPI
from app.routes import summarize, chat, preferences, history

app = FastAPI(title="ClearChoice Consent API")

app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(preferences.router, prefix="/preferences", tags=["Preferences"])
app.include_router(history.router, prefix="/history", tags=["History"])

@app.get("/")
def root():
    return {"message": "Consent Guardian API is running!"}
