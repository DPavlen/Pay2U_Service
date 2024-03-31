from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Services, Subscription, TariffList


class CategoryServicesInline(admin.TabularInline):
    """Таблица отношений Services - Category."""

    model = Services
    min_num = 0
    extra = 0


class TariffListInline(admin.TabularInline):
    """Таблица отношений TariffList - Services."""

    model = TariffList
    min_num = 0
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настроенная панель админки категории."""

    inlines = (CategoryServicesInline,)

    list_display = (
        "id",
        "name",
        "slug",
        "description",
        "icon",
        "display_icon",  # Добавляем метод display_icon в list_display
    )
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ("id", "name")
    search_fields = ("name",)

    def display_icon(self, obj):
        """Возвращает отображение иконки категории."""
        if obj.icon:
            return format_html(
                '<img src="{}" style="max-width:100px; '
                'max-height:100px"/>'.format(obj.icon.url)
            )
        return "-"

    display_icon.short_description = "Category Icon"


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление подписками)."""

    inlines = (TariffListInline,)

    list_display = (
        "id",
        "name",
        "category",
        "link",
        "description",
        "icon_big",
        "is_popular",
    )
    list_display_links = ("id", "name")
    search_fields = ("category__name",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Настроенная панель админки (управление подписками)."""

    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "tariff",
        "is_active",
    )
    list_display_links = ("id",)
    search_fields = ("service__name", "user")


@admin.register(TariffList)
class TariffListAdmin(admin.ModelAdmin):
    """Настроенная панель админки (тарифы к сервисам)."""

    list_display = (
        "id",
        "name",
        "description",
        "services",
        "services_duration",
        "tariff_full_price",
        "tariff_promo_price",
    )
    list_display_links = ("id",)
    search_fields = ("services__name", "services_duration")
