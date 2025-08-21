# app/core/auth.py
from fastapi import Depends, HTTPException, Header
from supabase import create_client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_current_user(authorization: str = Header(...)):
    """
    Extracts user from Supabase JWT token passed in Authorization header.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.split(" ")[1]

    try:
        user = supabase.auth.api.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
