from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Services, Subscription, TariffList


class CategoryServicesInline(admin.TabularInline):
    """
    Таблица отношений Services - Category.
    Attributes:
        model (Model): Модель связи между сервисами и категориями.
        min_num (int): Минимальное количество форм для отображения.
        extra (int): Дополнительное количество пустых форм.
    """

    model = Services
    min_num = 0
    extra = 0


class TariffListInline(admin.TabularInline):
    """
    Таблица отношений TariffList - Services.
    Attributes:
        model (Model): Модель связи между тарифами и сервисами.
        min_num (int): Минимальное количество форм для отображения.
        extra (int): Дополнительное количество пустых форм.
    """

    model = TariffList
    min_num = 0
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Настроенная панель админки категории.
    Attributes:
        inlines (tuple): Кортеж с инлайнами, отображаемыми на странице администратора.
        list_display (tuple): Поля для отображения в списке объектов категории.
        prepopulated_fields (dict): Автозаполняемые поля при создании категории.
        list_display_links (tuple): Поля, которые являются ссылками для отображения объекта.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """

    inlines = (CategoryServicesInline,)

    list_display = (
        "id",
        "name",
        "slug",
        "description",
        "icon",
        "display_icon",
    )
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ("id", "name")
    search_fields = ("name",)

    def display_icon(self, obj):
        """
        Возвращает отображение иконки категории.
        Args: obj (Category): Объект категории.
        Returns: str: HTML-код для отображения изображения.
        """

        if obj.icon:
            return format_html(
                '<img src="{}" style="max-width:100px; '
                'max-height:100px"/>'.format(obj.icon.url)
            )
        return "-"

    display_icon.short_description = "Category Icon"


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """
    Настроенная панель админки (управление подписками).
    Attributes:
        inlines (tuple): Кортеж с инлайнами, отображаемыми на странице администратора.
        list_display (tuple): Поля для отображения в списке объектов сервисов.
        list_display_links (tuple): Поля, которые являются ссылками для отображения объекта.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """

    inlines = (TariffListInline,)

    list_display = (
        "id",
        "name",
        "category",
        "link",
        "description",
        "icon_big",
        "icon_square",
        "icon_small",
        "is_popular",
    )
    list_display_links = ("id", "name")
    search_fields = ("category__name",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Настроенная панель админки (управление подписками).
    Attributes:
        list_display (tuple): Поля для отображения в списке объектов подписок.
        list_display_links (tuple): Поля, которые являются ссылками для отображения объекта.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """

    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "tariff",
        "is_active",
        "auto_payment"
    )
    list_display_links = ("id",)
    search_fields = ("service__name", "user")


@admin.register(TariffList)
class TariffListAdmin(admin.ModelAdmin):
    """
    Настроенная панель админки (тарифы к сервисам).
    Attributes:
        list_display (tuple): Поля для отображения в списке объектов тарифов.
        list_display_links (tuple): Поля, которые
        являются ссылками для отображения объекта.
        search_fields (tuple): Поля, по которым осуществляется поиск.
    """

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
