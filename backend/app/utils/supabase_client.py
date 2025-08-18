from supabase import create_client
import os

SUPABASE_URL = os.getenv("https://lcnfigfgrxedbkpmjdfl.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxjbmZpZ2ZncnhlZGJrcG1qZGZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU1NDUzNDksImV4cCI6MjA3MTEyMTM0OX0._jKIY6gI66ClQUlATAYVg6GEYGWTI72bxSpGzln_e3s")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
