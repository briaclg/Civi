from civiweb import models
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class GeographicZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GeographicZone
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        depth = 1
        fields = '__all__'
