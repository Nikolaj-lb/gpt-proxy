from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages")
    if not messages:
        return JSONResponse(content={"error": "Missing 'messages'"}, status_code=400)

    try:
        # Новый способ обращения к API
        response = openai.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return JSONResponse(content=response['choices'][0]['message'])
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# fix main.py
