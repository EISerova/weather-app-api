"""Вьюсеты для обработки запросов."""

from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from weather.models import Town, Subscribe

from .serializers import (
    SignUpSerializer,
    SubscribeSerializer,
    TokenSerializer,
    TownSerializer,
)


@api_view(["POST"])
@permission_classes([AllowAny])
def user_signup(request):
    """Регистрация пользователей и отправка кода подтвержения на почту."""

    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(subscriber=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def user_auth(request):
    """Получение пользователем токена."""

    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response("Токен выслан на указанную почту", status=status.HTTP_200_OK)


class SubscribeViewSet(viewsets.ModelViewSet):
    """Обрабатывает запрос к подпискам."""

    serializer_class = SubscribeSerializer

    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        """
        Создает подписку.
        Подписчик устанавливается автоматически,
        в запросе передается только автор.
        """
        serializer.save(subscriber=self.request.user)

    # def get_queryset(self):
    #     """Возвращает список подписок автора запроса."""
    #     user_id = self.request.user.id
    #     subscribes = Subscribe.objects.filter(subscriber_id=user_id).first()
    #     return subscribes

    def list(self, request):
        user_id = self.request.user.id
        queryset = Subscribe.objects.filter(subscriber_id=user_id)
        serializer = SubscribeSerializer(queryset, many=True)
        return Response(serializer.data)


class TownViewSet(viewsets.ModelViewSet):
    "Обрабатывает запрос по городам."

    serializer_class = TownSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Town.objects.all()
