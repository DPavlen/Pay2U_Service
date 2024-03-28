from django.contrib import admin
from services.models import Subscription

from .models import MyUser


class SubscriptionInline(admin.TabularInline):
    """Таблица отношений Subscription - User."""

    model = Subscription
    min_num = 0
    extra = 0


class BaseAdminSettings(admin.ModelAdmin):
    """Базовая настроенная админ панели."""

    empty_value_display = "-пусто-"
    list_filter = ("email", "username")


@admin.register(MyUser)
class UsersAdmin(BaseAdminSettings):
    """Настроенная панель админки (управление пользователями)."""

    inlines = (SubscriptionInline,)

    list_display = ("id", "role", "username", "email", "first_enter", "full_name")
    list_display_links = ("id", "username")
    search_fields = ("username", "role")
