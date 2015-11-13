from django.contrib import admin
from feedback.models import Feedback

class FeedbackDateTime(admin.ModelAdmin):
	
	'''
	FeedbackDateTime class used to specify the
	readonly_fields for the Feedback model
	inside the Django admin interface.
	'''
	
	readonly_fields = ("datetime_posted",)

admin.site.register(Feedback, FeedbackDateTime)