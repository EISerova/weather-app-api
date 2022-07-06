from rest_framework import serializers

from weather.models import Subscribe, Town
from .config_weather_api import create_town_for_subscribe, get_weather


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
