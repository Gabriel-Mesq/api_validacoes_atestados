import requests
from dotenv import load_dotenv
import os

load_dotenv()

def call_llama(bearer_token, prompt):
    url = "https://api.go.gov.br/ia/modelos-linguagem-natural/v2.0/generate"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9
        }
    }
    
    response = requests.post(url, json=data, headers=headers)

    print(f"🔹 Status Code: {response.status_code}")
    print(f"🔹 Headers: {response.headers}")
    print(f"🔹 Response Text:\n{response.text}")

    if response.status_code == 200:
        return {"response": response.text} 
    else:
        return {"error": response.status_code, "message": response.text}

bearer_token = os.getenv("TOKEN")
prompt = "Qual a utilidade de cada um desses modelos: llama3.2:3b, llama3.1:8b, llava:7b-v1.5-fp16, llama3.2-vision:11b?"
response = call_llama(bearer_token, prompt)
print(response["response"])


