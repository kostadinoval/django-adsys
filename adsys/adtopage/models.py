from django.db import models
from advert.models import Advert
from page.models import Page

class AdToPage(models.Model):
	advert = models.ForeignKey(Advert)
	page = models.ForeignKey(Page)
	active = models.BooleanField(default = False)
	
	def __unicode__(self):
		return str(self.advert.pk) + " - " + str(self.page.pk)
