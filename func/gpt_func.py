import flask
from flask import Flask
import requests
import json


def extract_text(json_string):
    try:
        data = json.loads(json_string)
        text_message = data['result']['alternatives'][0]['message']['text']
        return text_message
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        return f"Error extracting text: {str(e)}"


def give_response(question):
    req = {
        "modelUri": "ds://bt1c6uef35akirccs3k0",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты — умный ассистент."
            },
            {
                "role": "user",
                "text": question
            }
        ]
    }
    headers = {"Authorization": "Api-Key " + 'AQVN2BuID21OjoNTpNTBjZT9laLbmNEDUra2iSO3',
               }
    res = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                        headers=headers, json=req)
    answer = res.json()
    return answer['result']['alternatives'][0]['message']['text']

