import constants

from openai import OpenAI

#Initialize OLLAMA
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.1:latest"
ollama = OpenAI(base_url=constants.OLLAMA_BASE_URL, api_key='ollama')

CHAT_SYSTEM_MESSAGE = """
You are Calculation expert. You need to help your client with complex calculations
"""


def getChatResponse(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": CHAT_SYSTEM_MESSAGE}] + history + [{"role": "user", "content": message}] 
    response = ollama.chat.completions.create(model=constants.MODEL, messages=messages)
    print(f"Content received from LLM {response.choices[0].message.content}")
    return response.choices[0].message.content