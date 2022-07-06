from celery import shared_task
from api.config import API_URL, appid
import requests

from weather.send_email import send_weather_mail
from .models import Subscribe, Town


@shared_task
def send_mail_task(hour):
    subscribes = Subscribe.objects.filter(update_period=hour)
    for subscribe in subscribes:
        weather = Town.objects.get(name=subscribe.town)
        email = subscribe.subscriber.email
        send_weather_mail(str(weather), [email])


@shared_task
def update_weather():
    towns = Town.objects.all()
    for town in towns:
        response = requests.get(
            API_URL,
            params={"q": town.name, "key": appid, "lang": "ru"},
        ).json()
        town.temp = response["current"]["temp_c"]
        town.feels_like = response["current"]["feelslike_c"]
        town.pressure = response["current"]["pressure_mb"]
        town.save(update_fields=["temp", "feels_like", "pressure"])
