""" A simple chat app with FastAPI. Powered by LLM models."""

from typing import Callable

from fastapi import FastAPI, HTTPException, Request, Depends, status

from chatter import get_chatter, models


app = FastAPI()

@app.get('/health')
async def health():
    return{
        "application": "Simple LLM API.",
        "message": "running successfully",
    } 

@app.post('/chat')
async def generate_chat(request: Request, chatter: Callable = Depends(get_chatter)):
    query =  await request.json()
    try:
        model = query["model"]
        if model not in models:
            return {"error": "Select one model from llama-3.1-70b-versatile, llama-3.1-8b-instant or mixtral-8x7b-32768"}        
    except ValueError as e:
        return {"error": "Select one model from llama-3.1-70b-versatile, llama-3.1-8b-instant or mixtral-8x7b-32768"}        
    
    try:
        temperature = float(query["temperature"])
        if temperature > 2 or temperature < 0:
            return {"error": "Pass a number between 0 and 2"}
    except ValueError as e:
        return {"error": "Pass a valid number between 0 and 2"}        
    
    try:
        response = chatter(
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


