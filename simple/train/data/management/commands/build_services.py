from django.core.management.base import BaseCommand, CommandError
import data.utils

class Command(BaseCommand):
    args = ''
    help = 'build services'

    def handle(self, *args, **options):
        data.utils.build_all_services()

