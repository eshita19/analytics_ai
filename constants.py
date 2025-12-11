#Initialize OLLAMA
from openai import OpenAI
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.1:latest"
OLLAMA = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')