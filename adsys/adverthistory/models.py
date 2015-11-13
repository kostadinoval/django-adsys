from django.db import models
from advert.models import Advert

class AdvertImpression(models.Model):
	advert = models.ForeignKey(Advert)
	numberOfImpressions = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return "Advert: " + str(self.advert) + " - " + "Number of impressions: " + str(self.numberOfImpressions)

class AdvertClick(models.Model):
	advert = models.ForeignKey(Advert)
	numberOfClicks = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return "Advert: " + str(self.advert) + " - " + "Number of clicks: " + str(self.numberOfClicks)		
