import json

from django.core.management.base import BaseCommand
from services.models import TariffList


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            with open("data/tariff.json", encoding="utf-8-sig") as f:
                tariff_data = json.load(f)
                for tariff in tariff_data:
                    name = tariff.get("name")
                    description = tariff.get("description")
                    # services_id = tariff.get("services_id")
                    # # Проверяем наличие идентификатора services_id и его значение
                    # if services_id and isinstance(services_id, int) and services_id > 0:
                    #     # services_id присутствует и является положительным целым числом
                    #     service = Services.objects.get(id=services_id)
                    # elif Services.name:
                    #     # services_name указан
                    #     Services.name = Services.objects.get(name=Services.name)
                    # else:
                    #     # Ни services_id, ни services_name не указаны
                    #     print(
                    #         f"Предупреждение: Не указаны ни services_id, ни services_name для тарифа {name}. Тариф будет пропущен.")
                    #     continue

                    services_duration = tariff.get("services_duration")
                    if services_duration:
                        if services_duration == "Один месяц":
                            services_duration = TariffList.Duration.ONE_MONTH
                        elif services_duration == "Три месяца":
                            services_duration = TariffList.Duration.THREE_MONTHS
                        elif services_duration == "Шесть месяцев":
                            services_duration = TariffList.Duration.SIX_MONTHS
                        elif services_duration == "Один год":
                            services_duration = TariffList.Duration.ONE_YEAR
                    else:
                        services_duration = None
                    tariff_full_price = tariff.get("tariff_full_price")
                    tariff_promo_price = tariff.get("tariff_promo_price")

                    # Получаем связанный объект Services по идентификатору
                    # service = Services.objects.get(id=services_id)

                    TariffList.objects.get_or_create(
                        name=name,
                        description=description,
                        # services=service,
                        services_duration=services_duration,
                        tariff_full_price=tariff_full_price,
                        tariff_promo_price=tariff_promo_price,
                    )
        except Exception as e:
            raise Exception("Ошибка при загрузке 'Тарифов': {}".format(str(e)))
        return (
            "Загрузка 'Тарифов' произошла успешно!"
            " Обработка файла tariff.json завершена."
        )
