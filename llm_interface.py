import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")


def get_llm_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use appropriate model
        messages=messages,
        temperature=0.2,
    )
    return response["choices"][0]["message"]["content"]
