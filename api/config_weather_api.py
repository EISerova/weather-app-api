import random

import requests
from rest_framework_simplejwt.tokens import AccessToken

from weather.models import Town
from weather_app.settings import (CONFIRMATION_CODE_CHARACTERS,
                                  CONFIRMATION_CODE_LENGTH)

from .config import API_URL, appid


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


def create_confirmation_code():
    """Создние кода подтверждения."""

    code = "".join(
        random.choice(CONFIRMATION_CODE_CHARACTERS)
        for _ in range(CONFIRMATION_CODE_LENGTH)
    )
    return code


def get_tokens_for_user(user):
    """Получение токена для авторизации."""

    access = AccessToken.for_user(user)
    return {"token": str(access)}
