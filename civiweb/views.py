from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, GeographicZone, Country, \
    City, Contact, Offer
from .serializers import CompanySerializer, GeographicZoneSerializer, \
    CountrySerializer, CitySerializer, ContactSerializer, OfferSerializer
from .paginations import OfferResultsSetPagination


class ApiCompanyView(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        companies = set([e.nom for e in self.queryset])
        companies = sorted(companies)
        queryset = []
        for company in companies:
            queryset.append(Company.objects.filter(nom=company).first())
        return queryset


class ApiGeographicZoneView(ReadOnlyModelViewSet):
    queryset = GeographicZone.objects.all()
    serializer_class = GeographicZoneSerializer

    def get_queryset(self):
        geographicZones = set([e.nom for e in self.queryset])
        geographicZones = sorted(geographicZones)
        queryset = []
        for geographicZone in geographicZones:
            queryset.append(Company.objects.filter(nom=geographicZone).first())
        return queryset


class ApiCountryView(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        countries = set([e.nom for e in self.queryset])
        countries = sorted(countries)
        queryset = []
        for country in countries:
            queryset.append(Company.objects.filter(nom=country).first())
        return queryset


class ApiCityView(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        cities = set([e.nom for e in self.queryset])
        cities = sorted(cities)
        queryset = []
        for city in cities:
            queryset.append(Company.objects.filter(nom=city).first())
        return queryset


class ApiContactView(ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        contacts = set([e.nom for e in self.queryset])
        contacts = sorted(contacts)
        queryset = []
        for contact in contacts:
            queryset.append(Company.objects.filter(nom=contact).first())
        return queryset


class ApiOfferView(ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        offers = set([e.nom for e in self.queryset])
        offers = sorted(offers)
        queryset = []
        for offer in offers:
            queryset.append(Company.objects.filter(nom=offer).first())
        return queryset
