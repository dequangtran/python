import requests
import ssl

url = 'https://bcai-test.web.boeing.com/bcai-public-api/conversation'

global CLEAN_Chunks2 

headers = {
    'accept': 'application/json',
    'Authorization': 'Basic  MTcxNTQ4NjpkZjMxZGFlYS03ZDFkLTQ2ZjAtOGUyMS05ZDJiZmFiODAyNjE=',
    'Content-Type': 'application/json'
}

data = {
    "messages":[
        {
            "role": "system",
            "content":'''      '''

        },
        {
            "role": "user",
            "content":f"""     """,
        }
    ],
    "conversation_mode": [
        "default"
    ],
    "model": "gpt-4o-mini",
    "conversation_guid": "asdf123",
    "conversation_source": "bcai-api-system-identifier",
    "temperature": 0,
    "stream": False
}

response = requests.post(url, headers=headers, json=data, verify=False)
response_content = response.json()
print("Response content is", response_content)
message_content = response_content['choices'][0]['message']['content']
print("message content is", message_content)
