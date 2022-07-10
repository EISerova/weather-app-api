from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.response import Response

from weather.models import Subscribe, Town, User
from weather.send_email import send_singup_mail, send_token_mail
from weather_app.settings import CONFIRMATION_CODE_LENGTH

from .config_weather_api import (
    create_confirmation_code,
    create_town_for_subscribe,
    get_tokens_for_user,
    get_weather,
)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра и создания пользователей админом."""

    class Meta:
        fields = ("email",)
        model = User


class SignUpSerializer(serializers.Serializer):
    """Сериализатор для регистрации."""

    email = serializers.EmailField(max_length=254, allow_blank=False, allow_null=False)

    def create(self, validated_data):
        confirmation_code = create_confirmation_code()
        email = validated_data.get("email")

        try:
            user, created = User.objects.get_or_create(
                email=email,
                defaults={"confirmation_code": confirmation_code},
            )
        except IntegrityError:
            return Response(
                "Пользователь с такой почтой уже существует.",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not created:
            confirmation_code = user.confirmation_code

        send_singup_mail(email, confirmation_code)
        return user


class TokenSerializer(serializers.Serializer):
    """Сериализатор для создания токенов."""

    email = serializers.EmailField(max_length=254, allow_blank=False, allow_null=False)
    confirmation_code = serializers.CharField(max_length=CONFIRMATION_CODE_LENGTH)

    def create(self, validated_data):
        confirmation_code = validated_data.get("confirmation_code")
        email = validated_data.get("email")
        user = get_object_or_404(User, email=validated_data["email"])
        confirmation_code = validated_data.get("confirmation_code")
        if confirmation_code != user.confirmation_code:
            return Response(
                "Неверный код подтверждения", status=status.HTTP_400_BAD_REQUEST
            )
        token = get_tokens_for_user(user)
        send_token_mail(email, token.get("token"))
        return token

    class Meta:
        model = User
        fields = (
            "email",
            "confirmation_code",
        )


class TownSerializer(serializers.ModelSerializer):
    """Сериализатор для запросов по городам и погоды."""

    class Meta:
        model = Town
        fields = (
            "temp",
            "feels_like",
            "pressure",
            "name",
            "subscribe",
        )


class SubscribeSerializer(serializers.ModelSerializer):
    """Сериализатор для запросов по подпискам."""

    subscriber = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        subscribe = Subscribe.objects.create(**validated_data)
        town = validated_data.get("town")

        if not Town.objects.filter(name=town).exists():
            weather = get_weather(town)
            create_town_for_subscribe(weather, town, subscribe)

        return subscribe

    class Meta:
        model = Subscribe
        fields = (
            "subscriber",
            "town",
            "update_period",
        )
