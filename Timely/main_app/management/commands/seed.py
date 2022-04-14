import requests
from django.core.management.base import BaseCommand
from ...models import *


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

def get_token_countries():
    url = 'https://www.universal-tutorial.com/api/getaccesstoken'
    r = requests.get(url, params=None, headers={
    "Accept": "application/json",
    "api-token": "QZX-86Feq0Pkxbk0VRntPOaq7uS58qkEq1Iym7aMAAINRrDi1i8k6P6SMDAebSw3cbs",
    "user-email": "hanming497@gmail.com"
    }, cookies=None, auth=None, timeout=None)
    return r.json()


def get_countries():
    auth = get_token_countries()
    print(auth['auth_token'])
    url = 'https://www.universal-tutorial.com/api/countries'
    r = requests.get(url, params=None, headers={
    "Authorization": "Bearer " + auth['auth_token'],
    "Accept": "application/json"
}, cookies=None, auth=None, timeout=None)
    print("completed request")
    return r.json()

def seed_countries():
    print("seeding countries")
    for country in get_countries():
        country_obj = Country(country_name = country['country_name'], country_short_name = country['country_short_name'], country_phone_code = country['country_phone_code'])
        country_obj.save()

def clear_countries():
    Country.objects.all().delete()


def clear_timezones_table():
    Timezones.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        
        clear_timezones()
        clear_countries()
        clear_timezones_table()
        print("cleared previous data")
        seed_timezones()
        print("completed timezones")
        seed_countries()
        # clear_data()
        print("completed countries")

    



