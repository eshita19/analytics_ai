from constants import OLLAMA, MODEL

HIGHCHART_CONFIG_SYSTEM_MESSAGE  = """You are an expert in generating Highchart config. 
Given the type of Chart and Data points, you should generate the Highchart Config JSON.
You should only return the JSON.
 """
def getChatResponse(message):
    messages = [{"role": "system", "content": HIGHCHART_CONFIG_SYSTEM_MESSAGE}] + [{"role": "user", "content": message}] 
    response = OLLAMA.chat.completions.create(model=MODEL, messages=messages)
    print(f"Content received from LLM {response.choices[0].message.content}")
    return response.choices[0].message.content