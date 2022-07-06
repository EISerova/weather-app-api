"""Вьюсеты для обработки запросов."""

from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)

from .permissions import IsAuthorOrReadOnly
from .serializers import SubscribeSerializer, TownSerializer
from weather.models import Subscribe, Town


class SubscribeViewSet(viewsets.ModelViewSet):
    """Обрабатывает запрос к подпискам."""

    serializer_class = SubscribeSerializer

    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("subscriber__username",)

    def perform_create(self, serializer):
        """
        Создает подписку.
        Подписчик устанавливается автоматически,
        в запросе передается только автор.
        """
        serializer.save(subscriber=self.request.user)

    def get_queryset(self):
        """Возвращает список подписок автора запроса."""
        return self.request.user.subscriber


class TownViewSet(viewsets.ModelViewSet):
    "Обрабатывает запрос по городам."

    serializer_class = TownSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Town.objects.all()
