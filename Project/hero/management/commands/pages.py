from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('my command script')