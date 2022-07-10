from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models

from api.config import UPDATE_PERIODS
from weather_app.settings import CONFIRMATION_CODE_LENGTH

UPDATE_PERIODS_ERROR_MSG = "Выберите частоту рассылки - 1, 3, 6, или 12 часов."


def validate_update_period(value):
    if value not in UPDATE_PERIODS:
        raise ValidationError(UPDATE_PERIODS_ERROR_MSG)
    return value


class User(AbstractBaseUser):
    """Модель пользователей."""

    email = models.EmailField("почта", max_length=254, unique=True)
    confirmation_code = models.CharField(
        "Код подтверждения", max_length=CONFIRMATION_CODE_LENGTH, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Subscribe(models.Model):
    """Модель подписки."""

    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscribers",
        verbose_name="подписчик",
    )
    created = models.DateTimeField(auto_now_add=True)
    update_period = models.SmallIntegerField(
        default=12, validators=[validate_update_period]
    )
    town = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subscriber", "town"], name="subscriber_town_connection"
            )
        ]

    INFO_SUBSCRIBE = (
        "{subscriber} подписан на погоду в городе {town), "
        "частота рассылки - {update_period} часов."
    )

    def __str__(self) -> str:
        return self.INFO_SUBSCRIBE.format(
            subscriber=self.subscriber,
            town=self.town,
        )


class Town(models.Model):
    """Модель города."""

    temp = models.FloatField(default=None)
    feels_like = models.FloatField(default=None)
    pressure = models.SmallIntegerField(default=None)
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    subscribe = models.ForeignKey(
        Subscribe,
        on_delete=models.CASCADE,
        related_name="towns",
        verbose_name="подписка",
    )

    INFO_WEATHER = (
        "Погода. {name}: температура - {temp} градусов. "
        "Ощущается как {feels_like} градусов. "
        "Давление - {pressure}. Хорошего дня!"
    )

    def __str__(self) -> str:
        return self.INFO_WEATHER.format(
            name=self.name,
            temp=self.temp,
            feels_like=self.feels_like,
            pressure=self.pressure,
        )

    class Meta:
        ordering = ("name",)
