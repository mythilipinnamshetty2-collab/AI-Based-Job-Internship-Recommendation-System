import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("Key loaded:", key[:4] + "..." if key else "NO KEY FOUND")

url = "https://generativelanguage.googleapis.com/v1beta/models"

headers = {
    "x-goog-api-key": key
}

response = requests.get(url, headers=headers, timeout=30)

print("Status code:", response.status_code)
print("Response:")
print(response.text)