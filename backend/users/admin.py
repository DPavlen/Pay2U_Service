from django.contrib import admin

from .models import MyUser, UserIcon


class BaseAdminSettings(admin.ModelAdmin):
    """Базовая настроенная админ панели."""

    empty_value_display = "-пусто-"
    list_filter = ("email", "username")


@admin.register(MyUser)
class UsersAdmin(BaseAdminSettings):
    """Настроенная панель админки (управление пользователями)."""

    list_display = ("id", "role", "username", "email", "first_name", "last_name")
    list_display_links = ("id", "username")
    search_fields = ("username", "role")


class UserIconAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление пользователями)."""

    list_display = (
        "id",
        "user",
        "icon",
    )
    list_display_links = ("id", "user")
    list_filter = (
        "user__email",
        "user__username",
    )  # Используем атрибуты модели MyUser для фильтрации
    search_fields = ("user__id",)  # Также добавляем поиск по id пользователя


admin.site.register(UserIcon, UserIconAdmin)
