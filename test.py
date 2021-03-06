import django

import os
from django.db.models import Count, Sum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from civiweb.models import Country, Company, City, Contact, Offer

# Desc view counter
# print(Offer.objects.all().values().order_by('-viewCounter'))

# Order countries by number of viewer
# viewers = Offer.objects.all().values('country_id').annotate(aliquots=Count('country_id'), total=Sum('viewCounter')).order_by('-total')
# for viewer in viewers:
#     print(Country.objects.filter(id=viewer['country_id']))
#     print(viewer['total'])

# Order countries by number of candidate
candidates = Offer.objects.all().values('country_id').annotate(aliquots=Count('country_id'),
                                                               total=Sum('candidateCounter')).order_by('-total')
for candidate in candidates:
    country = Country.objects.filter(id=candidate['country_id']).annotate(num_offer=Count('offer'))[0]
    print(country.countryName)
    print("nombre d'offres: {}".format(country.num_offer))
    print("Total: {}".format(candidate['total']))
    print("Ratio: {} \n".format(candidate['total'] / country.num_offer))
