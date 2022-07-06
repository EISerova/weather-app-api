import requests
from .models import Weather
import time
import os

APPID = "619cf32b5766209f1f063fe5a4b3e5a0"  
URL_BASE = "http://api.openweathermap.org/data/2.5/"
RETRY_TIME = 10


def current_weather(q, appid) -> dict:
    """https://openweathermap.org/api"""
    return requests.get(URL_BASE + "weather", params=locals()).json()


def main():
    if not current_weather():
        raise ValueError('Ошибка подключения')
    while True:
        try:
            weather: dict = current_weather('Moscow', APPID)
            new = Weather(
                temp=weather['temp'],
                feels_like=weather['feels_like'],
                pressure=weather['pressure']        
            )
            new.save()
            print('ok')         
        except Exception as error:
            print(error)
        time.sleep(RETRY_TIME)

if __name__ == '__main__':
    basepath = os.path.dirname(__file__)
    main()



