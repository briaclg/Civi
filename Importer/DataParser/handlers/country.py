# Geographic zone
import django
import requests
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import GeographicZone, Country

# Countries
url = "https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/repository/geographic-zones/countries"
payload = "[0]"
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d; '
              'ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d '
}
response = requests.request("POST", url, headers=headers, data=payload)
countries = json.loads(response.text)

for country in countries:
    geographic_zone = GeographicZone.objects.filter(geographicCode=country['geographicZoneId'])[0]
    Country.objects.get_or_create(countryName=country['countryName'],
                                  countryNameEn=country['countryNameEn'],
                                  countryCode=country['countryId'],
                                  geographicZone=geographic_zone
                                  )
