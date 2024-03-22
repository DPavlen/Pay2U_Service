from django.contrib import admin
from Pay2U_Service.backend.services.models import Services


@admin.register(Services)
class UsersAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление пользователями)."""

    list_display = (
        "id",
        "name",
        "category",
        "services_duration",
        "cost",
        "subscription_type",
    )
    list_display_links = ("id", "name")
    search_fields = ("category",)
