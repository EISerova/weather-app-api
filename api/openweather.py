import requests
from models import Weather

APPID = "619cf32b5766209f1f063fe5a4b3e5a0"  
URL_BASE = "http://api.openweathermap.org/data/2.5/"


def current_weather(q: str = "Moscow", appid: str = APPID) -> dict:
    """https://openweathermap.org/api"""
    return requests.get(URL_BASE + "weather", params=locals()).json()


# def weather_forecast(q: str = "Kolkata, India", appid: str = APPID) -> dict:
#     """https://openweathermap.org/forecast5"""
#     return requests.get(URL_BASE + "forecast", params=locals()).json()


# def weather_onecall(lat: float = 55.68, lon: float = 12.57, appid: str = APPID) -> dict:
#     """https://openweathermap.org/api/one-call-api"""
#     return requests.get(URL_BASE + "onecall", params=locals()).json()


# if __name__ == "__main__":
#     from pprint import pprint
        
while True:
    location = input("Enter a location:").strip()
    weather = current_weather(location)['main']
    new = Weather(
        temp=weather['temp'],
        feels_like=weather['feels_like'],
        pressure=weather['pressure']        
    )
    new.save()
    if location:
        pprint(current_weather(location)['main'])
        # pprint(current_weather(location))
    else:
        break