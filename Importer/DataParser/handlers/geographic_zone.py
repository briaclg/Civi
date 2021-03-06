# Geographic zone
import django
import requests
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import GeographicZone

url = "https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/repository/geographic-zones?page=1"

payload = {}
headers = {
    'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d; ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d'
}
response = requests.request("GET", url, headers=headers, data=payload)
zones = json.loads(response.text)

for zone in zones['result']:
    GeographicZone.objects.get_or_create(geographicZoneLabel=zone['geographicZoneLabel'],
                                         geographicZoneLabelEn=zone['geographicZoneLabelEn'],
                                         geographicCode=zone['geographicZoneId'],
                                         );