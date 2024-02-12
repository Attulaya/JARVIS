import requests
import socket
from google_search_scraper import GoogleSearchScraper  # Import the GoogleSearchScraper class

def google_search_and_scrape(query):
    """
    Perform a Google search on the given query and scrape text from the search results.

    Parameters:
        query (str): The search query.

    Returns:
        str: The combined text scraped from the search results.
    """
    return GoogleSearchScraper.google_search(query)



def chat1(chat):
    messages = []  # list in which all messages are stored
    system_message = f"you are an AI bot that can do everything using function call and other information also. when you are asked to do something  use the function call you have available and then respond with message, your name is Jarvis  and your creator is attulaya, find the content related to the query: user query "
    message = {"role": "user", "parts":  [{"text": system_message+" "+chat}]}
    messages.append(message)
    data = {"contents": messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=yourapikey"
    response = requests.post(url, json=data)
    t1 = response.json()
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    return t2
def get_ip(host):
    try:
        result= socket.getaddrinfo(host,None)
    except Exception as e:
        print(e)
        result=f"error in finding the ip {e}"
    return result
def temp_room(room):
    result = "temp = 20, humidity = 70"
    return result
def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "c"}

    headers = {
        "X-RapidAPI-Key": "yourapikey",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    try:
        response.raise_for_status()  # Check for any HTTP errors
        d1 = response.json()
        d2 = d1.get("current_observation")
        if d2:
            hum = d2.get('atmosphere', {}).get("humidity")
            temp = d2.get('condition', {}).get("temperature")
            if hum is not None and temp is not None:
                return (f"Humidity: {hum}, Temperature in Celsius: {temp}")
            else:
                print("Unable to retrieve humidity and temperature.")
        else:
            print("No current observation data available.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

defination= [

    {
    "name" : "temp_city", # name of the function to be called
    "description" : "find weather, temperature of a city",
    "parameters" :
        {
            "type" : "object",
            "properties":
                        {
                            "city": # arguments for function temp_city
                                {
                                    "type" : "string",
                                    "description": "city to find weather"

                                }

                        }
        }


    },
    {
    "name" : "temp_room", # name of the function to be called
    "description" : "find temperature of my room or my home",
    "parameters" :
        {
            "type" : "object",
            "properties":
                        {
                            "room": # arguments for function temp_city
                                {
                                    "type" : "string",
                                    "description": "room or home"

                                }

                        }
        }


    },
{
    "name" : "get_ip", # name of the function to be called
    "description" : "find  ip address of given url or domain name",
    "parameters" :
        {
            "type" : "object",
            "properties":
                        {
                            "host": # arguments for function temp_city
                                {
                                    "type" : "string",
                                    "description": "get url or domain"

                                }

                        }
        }


    },
{
    "name" : "chat1", # name of the function to be called
    "description" : "hi hello",
    "parameters" :
        {
            "type" : "object",
            "properties":
                        {
                            "chat": # arguments for function temp_city
                                {
                                    "type" : "string",
                                    "description": "full query asked by user"

                                }

                        }
        }


    },
    {
        "name": "google_search_and_scrape",
        "description": "Perform a Google search ",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "search query"
                }
            }
        }
    }
    ]

if __name__ == "__main__":
    print(temp_city("bangalore"))
