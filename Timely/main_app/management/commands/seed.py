import requests
from django.core.management.base import BaseCommand
from ...models import iana_timezones


def get_iana_timezones():
    url = 'https://timeapi.io/api/TimeZone/AvailableTimeZones'
    r = requests.get(url)
    return r.json()

def seed_timezones():
    for zone in get_iana_timezones():
        timezone = iana_timezones(iana_timezone=zone)
        timezone.save()


def clear_timezones():
    iana_timezones.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_timezones()
        # clear_data()
        print("completed")

