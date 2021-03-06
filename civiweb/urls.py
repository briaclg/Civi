from .views import ApiCompanyView, ApiGeographicZoneView, \
    ApiCountryView, ApiCityView, ApiContactView, ApiOfferView
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register('api/company', ApiCompanyView)
router.register('api/geographicZone', ApiGeographicZoneView)
router.register('api/country', ApiCountryView)
router.register('api/city', ApiCityView)
router.register('api/contact', ApiContactView)
router.register('api/offer', ApiOfferView)

urlpatterns = [
    path('', include(router.urls))
]
