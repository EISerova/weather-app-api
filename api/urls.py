"""Роутеры к API-запросам."""

from django.urls import include, path
from rest_framework import routers

from .views import SubscribeViewSet, UpdateSubscribeSet, user_auth, user_signup

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register(r"subscribe", SubscribeViewSet, basename="subscribe")
router_v1.register(
    r"subscribe/(?P<subscribe_id>\d+)", UpdateSubscribeSet, basename="update_subscribe"
)

urlpatterns = [
    path("v1/auth/signup/", user_signup),
    path("v1/auth/token/", user_auth),
    path("v1/", include(router_v1.urls)),
]
