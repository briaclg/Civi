import django
import os
from django.utils import dateparse
from django.utils.timezone import make_aware
from geopy import Nominatim
from slugify import slugify

from Importer.handlers.base import BaseDataFormat

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import Country, Company, City, Contact, Offer


def xnone(s):
    if s == '':
        return None
    return s

# URL for details
# https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/details/148340


class OfferImport(BaseDataFormat):
    METHOD = 'POST'
    URL = 'https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/latest'
    PAYLOAD = '{\"skip\":0,\"limit\":10000}'
    HEADERS = {
        'Content-Type': 'application/json',
        'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d; '
                  'ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d'
    }

    def parse(self, data):
        """
        Parse the request
        """
        all_offers_active = []

        for offer in data['result']:
            print(offer)
            company, created_company = Company.objects.get_or_create(
                organizationName=offer['organizationName'],
                ca=offer['ca'],
                effectif=offer['effectif'],
                organizationPresentation=offer['organizationPresentation'],
                organizationCountryCounter=xnone(offer['organizationCountryCounter']),
                organizationExpertise=offer['organizationExpertise'],
                organizationCode=offer['organizationId'])

            country = Country.objects.filter(countryName=offer['countryName'])[0]
            city, created_city = City.objects.get_or_create(
                cityName=offer['cityName'],
                cityNameEn=offer['cityNameEn'],
                country=country)

            # Here we find geo coordinates of the city
            if created_city:
                geolocator = Nominatim(user_agent="civiweb")
                slug = 'a-definir'
                slugEng = 'to-be-define'
                adress = city.cityName
                if slugify(adress) != slug and slugify(adress) != slugEng:
                    location = geolocator.geocode(adress)
                    if location:
                        city.latitude = location.latitude
                        city.longitude = location.longitude
                        city.save()


            contact, created_contact = Contact.objects.get_or_create(
                contactName=offer['contactName'],
                contactEmail=offer['contactEmail'],
                organization=company)


            offer_object, offer_created = Offer.objects.update_or_create(
                offerCode=offer['id'],
                defaults={
                    'offerCode': offer['id'],
                    'active': True,
                    'missionTitle': offer['missionTitle'],
                    'missionDuration': offer['missionDuration'],
                    'viewCounter': offer['viewCounter'],
                    'candidateCounter': offer['candidateCounter'],
                    'missionType': offer['missionType'],
                    'missionTypeEn': offer['missionTypeEn'],
                    'missionDescription': offer['missionDescription'],
                    'creationDate': make_aware(dateparse.parse_datetime(offer['creationDate'])),
                    'missionStartDate': make_aware(dateparse.parse_datetime(offer['missionStartDate'])),
                    'missionEndDate': make_aware(dateparse.parse_datetime(offer['missionEndDate'])),
                    'startBroadcastDate': make_aware(dateparse.parse_datetime(offer['startBroadcastDate'])),
                    'durationBroadcast': offer['durationBroadcast'],
                    'missionProfile': offer['missionProfile'],
                    'reference': offer['reference'],
                    'indemnite': offer['indemnite'],
                    'idMotifDesactivationOffre': offer['idMotifDesactivationOffre'],
                    'country': country,
                    'contact': contact,
                    'city': city,
                    'organization': company
                },
            )
            # See last offer
            if dateparse.parse_datetime(offer['creationDate']) >= dateparse.parse_datetime('2021-03-25T16:00:00.00')\
                    or dateparse.parse_datetime(offer['startBroadcastDate']) > dateparse.parse_datetime('2021-03'
                                                                                                        '-25T00:00:00'
                                                                                                        '.00'):
                print(True)
            all_offers_active.append(offer_object.offerCode)

        Not_active_offers = Offer.objects.exclude(offerCode__in=all_offers_active)

        for na_offers in Not_active_offers:
            na_offers.active = False
            na_offers.save()