import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()

def call_llama_vision(bearer_token, image_path, prompt):
    url = "https://api.go.gov.br/ia/modelos-linguagem-natural/v2.0/generate"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    data = {
        "model": "llama3.2-vision:11b",
        "prompt": prompt,
        "images": [image_base64],  
        "options": {
            "temperature": 0.7,
            "top_p": 0.9
        }
    }

    response = requests.post(url, json=data, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Response Text:\n{response.text}")

    if response.status_code == 200:
        return {"response": response.text}  
    else:
        return {"error": response.status_code, "message": response.text}

image_path = "ANA CAROLINA DE CASTRO BUENO 12.02.2025.jpeg" 
bearer_token = os.getenv("TOKEN")
prompt = "Responda apenas com o nome completo da paciente no atestado médico."
response = call_llama_vision(bearer_token, image_path, prompt)
