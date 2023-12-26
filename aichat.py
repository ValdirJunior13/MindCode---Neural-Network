import requests

def chatmessage(message, user, channel):
    api_base = "http://localhost:8000/v1/chat/completions"
    model = "fastchat-t5-3b-v1.0"
    prompt ={
        "model": model,
        "message":[{"role": "user", "content": "${message}"}]
        }
    print("a msg foi enviada"+message)
    response = requests.post(api_base, json=prompt)
    return response.json()
   
      
