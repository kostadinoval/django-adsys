from django.contrib import admin
from adspace.models import AdSpace

class AdSpaceDate(admin.ModelAdmin):
	
	'''
	AdSpaceDate class used to specify the
	readonly_fields for the AdSpace model
	inside the Django admin interface.
	'''
	
	readonly_fields = ("datetime_posted",)

admin.site.register(AdSpace, AdSpaceDate)