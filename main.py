from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/process")
async def process(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    if not prompt:
        return {"error": "Missing prompt"}

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"response": response.choices[0].message["content"]}
