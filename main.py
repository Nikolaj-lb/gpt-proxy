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
        # Новый способ обращения к OpenAI API с корректными параметрами
        response = openai.Completion.create(
            model="text-davinci-003",  # Для совместимости с новым API
            prompt=messages[0]['content'],  # Используем первый message как prompt
            max_tokens=150
        )
        return JSONResponse(content={"response": response['choices'][0]['text']})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# fix main.py
