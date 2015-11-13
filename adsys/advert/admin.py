from django.contrib import admin
from advert.models import Advert, AdvertKeyword

class AdvertDateTime(admin.ModelAdmin):
	
	'''
	AdvertDateTime class used to specify the
	readonly_fields for the Advert model
	inside the Django admin interface.
	'''
	
	readonly_fields = ("datetime_posted",)

admin.site.register(Advert, AdvertDateTime)
admin.site.register(AdvertKeyword)
