import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_app.settings")
app = Celery("weather_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    "update_weather": {
        "task": "weather.tasks.update_weather",
        "schedule": crontab(minute="*/55"),
    },
    "send_weather_one_hour": {
        "task": "weather.tasks.send_mail_task",
        "schedule": crontab(minute=0, hour="*/1"),
        "args": (1,),
    },
    "send_weather_three_hour": {
        "task": "weather.tasks.send_mail_task",
        "schedule": crontab(minute=0, hour="*/3"),
        "args": (3,),
    },
    "send_weather_six_hour": {
        "task": "weather.tasks.send_mail_task",
        "schedule": crontab(minute=0, hour="*/6"),
        "args": (6,),
    },
    "send_weather_twelve_hour": {
        "task": "weather.tasks.send_mail_task",
        "schedule": crontab(minute=0, hour="*/12"),
        "args": (12,),
    },
}


# app.conf.result_chord_join_timeout = 900
# app.conf.result_chord_retry_interval = 5
# app.conf.result_expires = timedelta(days=3)
