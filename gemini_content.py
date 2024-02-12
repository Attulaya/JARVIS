from config import key
import requests  # web_library
from mic_to_text import mic1
def chat1(chat):
    messages = []  # list in which all messages are stored
    system_message = "you are an AI bot, your name is Jarvis"
    message = {"role": "user", "parts":  [{"text": system_message+" "+chat}]}
    messages.append(message)
    data = {"contents": messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyAoDuXAvi8rwECZMf2I874p6AWIcS72V8I"
    response = requests.post(url, json=data)
    t1 = response.json()
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

if __name__ == "__main__":
    chat = mic1()
    chat1(chat)