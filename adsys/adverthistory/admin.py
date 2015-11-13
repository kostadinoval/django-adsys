from django.contrib import admin
from adverthistory.models import AdvertImpression, AdvertClick

admin.site.register(AdvertImpression)
admin.site.register(AdvertClick)