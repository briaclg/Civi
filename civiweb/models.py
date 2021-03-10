from django.db import models


class Company(models.Model):
    organizationName = models.CharField(max_length=254)
    ca = models.IntegerField(null=True)
    effectif = models.IntegerField(null=True)
    organizationPresentation = models.CharField(max_length=254, null=True)
    organizationCountryCounter = models.IntegerField(null=True)
    organizationExpertise = models.CharField(max_length=254, null=True)
    organizationCode = models.IntegerField()

    def __str__(self):
        return str(self.organizationName) if self.organizationName else ''


class GeographicZone(models.Model):
    geographicZoneLabel = models.CharField(max_length=254)
    geographicZoneLabelEn = models.CharField(max_length=254)
    geographicCode = models.IntegerField()

    def __str__(self):
        return str(self.geographicZoneLabel) if self.geographicZoneLabel else ''


class Country(models.Model):
    countryName = models.CharField(max_length=254)
    countryNameEn = models.CharField(max_length=254, null=True)
    countryCode = models.IntegerField()
    geographicZone = models.ForeignKey(GeographicZone, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.countryName) if self.countryName else ''


class City(models.Model):
    cityName = models.CharField(max_length=254)
    cityNameEn = models.CharField(max_length=254, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.cityName) if self.cityName else ''


class Contact(models.Model):
    contactName = models.CharField(max_length=254, null=True)
    contactEmail = models.CharField(max_length=508, null=True)
    organization = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.contactName) if self.contactName else ''


class Offer(models.Model):
    offerCode = models.CharField(max_length=254)
    active = models.BooleanField()
    missionTitle = models.CharField(max_length=508)
    missionDuration = models.IntegerField()
    missionProfile = models.CharField(max_length=10000, null=True)
    viewCounter = models.IntegerField()
    candidateCounter = models.IntegerField()
    missionType = models.CharField(max_length=254, null=True)
    missionTypeEn = models.CharField(max_length=254, null=True)
    missionDescription = models.CharField(max_length=10000, null=True)
    creationDate = models.DateTimeField(null=True)
    missionStartDate = models.DateTimeField(null=True)
    missionEndDate = models.DateTimeField(null=True)
    startBroadcastDate = models.DateTimeField(null=True)
    durationBroadcast = models.IntegerField()
    reference = models.CharField(max_length=254, null=True)
    indemnite = models.IntegerField()
    idMotifDesactivationOffre = models.IntegerField()
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.missionTitle) if self.missionTitle else ''
