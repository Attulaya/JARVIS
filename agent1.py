# agent.py

import task
import requests
from mic_to_text import mic1

def parse_function_response(message):
    function_call = message[0].get("functionCall")
    function_name = function_call["name"]
    print("Gemini: call function", function_name)
    try:
        arguments = function_call.get("args")
        print("gemini arguments are", arguments)
        if arguments:
            d = getattr(task, function_name)
            print("function is ", d)
            function_responses = d(**arguments)
        else:
            function_responses = "no arguments are present"
    except Exception as e:
        print(e)
        function_responses = "Invalid Function"
    return function_responses

def run_conversation(user_message):
    messages = []  # list in which all messages are stored
    print(user_message)
    system_message = "you are an AI bot that can do everything using function call and other information also. when you are asked to do something  use the function call you have available and then respond with message, your name is Jarvis  and your creator is attulaya, always be accurate and always try to provide the outcomes to the user in anyway possible "
    message = {"role": "user", "parts": [{"text": system_message + "\n " + user_message}]}
    messages.append(message)
    data = {"contents": [messages],
            "tools": [{"functionDeclarations": task.defination}]}

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyAoDuXAvi8rwECZMf2I874p6AWIcS72V8I"  # Replace YOUR_API_KEY with your actual API key
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(response.text)
    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("error:no content in response")

    message = t1.get("candidates")[0].get("content").get("parts")
    if "functionCall" in message[0]:
       resp1 = parse_function_response(message)
       return resp1
    else:
        print("no function call")

if __name__ == "__main__":
    while True:  # Keep the interaction loop running indefinitely
        user_message = mic1()
        if user_message.strip().lower() == "exit":  # Terminate the loop if user inputs "exit"
            print("Exiting...")
            break
        response = run_conversation(user_message)
        print(response)
