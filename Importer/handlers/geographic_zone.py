# Geographic zone
import django
import os

from Importer.handlers.base import BaseDataFormat

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import GeographicZone


class GeographicZoneImport(BaseDataFormat):

    METHOD = 'GET'
    URL = 'https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/repository/geographic-zones?page=1'
    PAYLOAD = {}
    HEADERS = {
        'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d;'
                  ' ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d'
    }

    def parse(self, data):
        """
        Parse the request
        """

        for zone in data['result']:
            GeographicZone.objects.get_or_create(geographicZoneLabel=zone['geographicZoneLabel'],
                                                 geographicZoneLabelEn=zone['geographicZoneLabelEn'],
                                                 geographicCode=zone['geographicZoneId'],
                                                 )
