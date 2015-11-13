from django.db import models
from page.models import Page
from advert.models import Advert

class AdScore(models.Model):
	page = models.ForeignKey(Page)
	advert = models.ForeignKey(Advert)
	score = models.DecimalField(max_digits=5, decimal_places=4)
	
	def __unicode__(self):
		return "AdScore: " + str(self.page.pk) + " - " + str(self.advert.pk) + " - " + str(self.score)