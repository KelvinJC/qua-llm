""" A simple chat app with FastAPI. Powered by LLM models."""

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from chatter import send_chat_request, models

app = FastAPI()

@app.get('/health')
async def health():
    return{
        "application": "Simple LLM API.",
        "message": "running successfully",
    } 

@app.post('/chat')
async def generate_chat(request: Request):
    query =  await request.json()
    model = models[1]
    try:
        temperature = float(query["temperature"])
        if temperature > 2 or temperature < 0:
            return {"error": "Pass a number between 0 and 2"}
    except ValueError as e:
        return {"error": "Pass a valid number between 0 and 2"}        

    try:
        response = send_chat_request(
            model=model,
            query=query["question"],
            temperature=temperature,
        )
        return {
            "status": "success",
            "response": response,
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e),
        )


