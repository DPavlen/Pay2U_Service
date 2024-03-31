from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("add_сategory")
        call_command("add_tariff")
        call_command("add_service")
