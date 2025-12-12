from constants import OLLAMA, MODEL

CHAT_SYSTEM_MESSAGE = """
You are Data Analytics expert. Using tools you can help in generating desired result to user.
"""

get_contact_center_data = {
    "name": "get_contact_center_data",
    "description": "Get Data related to Contact Center. It could be data related to Agent and/or Supervisor.",
}

get_chart_config = {
    "name" : "get_chart_config",
    "description": "Given data in json format. Returns the HighChart config in JSON format.",
    "parameters": {
        "type": "object",
        "properties": {
            "chart_type": {
                "type": "string",
                "description": "The type of Chart Line, Bar or Pie",
            },
        },
        "required": ["chart_type"],
        "additionalProperties": False
    }
}
tools = [get_contact_center_data, get_chart_config]

def getChatResponse(message, history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": CHAT_SYSTEM_MESSAGE}] + history + [{"role": "user", "content": message}] 
    response = OLLAMA.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    print(f"Content received from LLM {response.choices[0].message.content}")
    message = response.choices[0].message
    
    return response.choices[0].message.content