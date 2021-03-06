from django.contrib import admin
from .models import Company, GeographicZone, Country,\
    City, Contact, Offer

# Register your models here.
admin.site.register(Company)
admin.site.register(GeographicZone)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Contact)
admin.site.register(Offer)
