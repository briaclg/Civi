import io
import json
import requests

from Importer.handlers.country import CountryImport
from Importer.handlers.geographic_zone import GeographicZoneImport
from Importer.handlers.offer import OfferImport

# List available data formats
importers = [
    GeographicZoneImport,
    CountryImport,
    OfferImport
]

for importer in importers:
    print('HEY')
    response = requests.request(importer.METHOD, importer.URL, headers=importer.HEADERS,
                                data=importer.PAYLOAD)
    data = json.loads(response.text)
    importer.parse(self=None, data=data)

