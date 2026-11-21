import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("success, gemini API key loaded.")
else:
    print("API key not found. check your .env file.")