from django.contrib import admin
from users.models import MyUser

from .models import Category, Services, Subscription


class CategoryServicesInline(admin.TabularInline):
    """Таблица отношений Services - Category."""

    model = Services
    min_num = 0
    extra = 0


class MyUserServicesInline(admin.TabularInline):
    """Таблица отношений User - Services."""

    model = MyUser
    min_num = 0
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настроенная панель админки категории."""

    inlines = (CategoryServicesInline,)

    list_display = (
        "id",
        "name",
        "description",
        "icon",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление подписками)."""

    #    inlines = (MyUserServicesInline,)

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


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление подписками)."""

    #    inlines = (MyUserServicesInline,)

    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "service",
        "status",
    )
    list_display_links = ("id",)
    search_fields = ("category", "user")
