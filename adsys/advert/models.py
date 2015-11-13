from django.db import models
from django.contrib.auth.models import User

class Advert(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=80)
	description = models.CharField(max_length=300)
	destination_url = models.CharField(max_length=140)
	datetime_posted = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.title
		
class AdvertKeyword(models.Model):
	advert = models.ForeignKey(Advert)
	keyword = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.keyword