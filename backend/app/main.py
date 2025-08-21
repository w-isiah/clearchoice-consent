# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import summarize, chat, preferences, history

# 1. Initialize FastAPI
app = FastAPI(title="Consent Guardian API")

# 2. Enable CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # React or frontend dev server
    "http://127.0.0.1:3000",
    "*",  # ⚠️ Allow all origins (for hackathon/demo only)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Include routers
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(preferences.router, prefix="/preferences", tags=["Preferences"])
app.include_router(history.router, prefix="/history", tags=["History"])

# 4. Root endpoint
@app.get("/")
def root():
    return {"message": "Consent Guardian API is running!"}
