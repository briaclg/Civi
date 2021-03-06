import django
import requests
import os
import json
from django.utils import dateparse
from django.utils.timezone import make_aware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import Country, Company, City, Contact, Offer


# Dataset url = "https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/repository/search/dataset" headers = {
# 'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d;
# ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d' } response =
# requests.request("GET", url, headers=headers) print(response.text)

def xnone(s):
    if s == '':
        return None
    return s


# Load all offers
url = "https://civiweb-api-offre-prd.azurewebsites.net/api/Offers/latest"
payload = "{\"skip\":0,\"limit\":10000}"
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'ARRAffinity=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d; ARRAffinitySameSite=92c475eedd41771f9c6f8d7f8c52ad11b610d1d082a92269eb132b8b216a0d8d'
}
response_offer = requests.request("POST", url, headers=headers, data=payload)
offers = json.loads(response_offer.text)

for offer in offers['result']:
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
    contact, created_contact = Contact.objects.get_or_create(
        contactName=offer['contactName'],
        contactEmail=offer['contactEmail'],
        organization=company)

    offer_update, created_offer = Offer.objects.update_or_create(
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

    if dateparse.parse_datetime(offer['creationDate']) > dateparse.parse_datetime('2021-06-03T00:00:00.00'):
        print(True)
