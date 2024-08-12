import uvicorn
from api import app


if __name__ == "__main__":
    print("Starting LLM API server.")
    uvicorn.run('api:app', host="127.0.0.1", port=8888, reload=True)