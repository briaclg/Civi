# Geographic zone
import django
import os

from Importer.handlers.base import BaseDataFormat

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import GeographicZone, Country


class CountryImport(BaseDataFormat):

    METHOD = 'POST'
    URL = 'https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/repository/geographic-zones/countries'
    PAYLOAD = '[0]'
    HEADERS = {
        'Content-Type': 'application/json',
        'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d;'
                  ' ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d '
    }

    def parse(self, data):
        """
        Parse the request
        """

        for country in data:
            geographic_zone = GeographicZone.objects.filter(geographicCode=country['geographicZoneId'])[0]
            Country.objects.get_or_create(countryName=country['countryName'],
                                          countryNameEn=country['countryNameEn'],
                                          countryCode=country['countryId'],
                                          geographicZone=geographic_zone
                                          )
