"""Роутеры к API-запросам."""

from django.urls import include, path
from rest_framework import routers

from .views import SubscribeViewSet, TownViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register(r"subscribe", SubscribeViewSet, basename="subscribe")
router_v1.register(r"towns", TownViewSet, basename="towns")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]