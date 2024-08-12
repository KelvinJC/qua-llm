"""Build a simple LLM application"""

import os
import groq
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
groq_client = groq.Groq(api_key=GROQ_API_KEY)
models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768",
]

def send_chat_request(model, query, temperature=0):
    sys_prompt = """You are a helpful virtual assistant. Your name is Ada.
    Your goal is to provide useful and relevant responses to my requests."""

    response = groq_client.chat.completions.create(
        model = model,
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": query},
        ],
        response_format = {"type": "text"},
        temperature = temperature # accuracy is higher with temp closer to 0. Creativity is higher as value tends towards 1. Higher chance of hallucination
    )
    answer = response.choices[0].message.content
    return answer


