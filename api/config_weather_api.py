from weather.models import Town
from .config import API_URL, appid
import requests


def create_town_for_subscribe(response, town, subscribe):
    """Создание объекта погоды."""

    API_RESPONSE_FIELDS = {
        "temp": response["current"]["temp_c"],
        "feels_like": response["current"]["feelslike_c"],
        "pressure": response["current"]["pressure_mb"],
    }

    Town.objects.create(
        temp=API_RESPONSE_FIELDS["temp"],
        feels_like=API_RESPONSE_FIELDS["feels_like"],
        pressure=API_RESPONSE_FIELDS["pressure"],
        name=town,
        subscribe=subscribe,
    )


def get_weather(town):
    """Создание объекта погоды."""

    response = requests.get(
        API_URL,
        params={
            "q": town,
            "key": appid,
            "lang": "ru",
        },
    ).json()
    return response
