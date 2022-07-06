from django.contrib import admin

from weather.models import Subscribe, Town


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "created",
        "subscriber_id",
    )
    search_fields = ("subscriber_id",)


class TownAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_editable = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Town, TownAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
