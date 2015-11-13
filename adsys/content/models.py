from django.db import models
from page.models import Page

class Keyword(models.Model):
	keyword = models.CharField(max_length=30, unique=True)
	
	def __unicode__(self):
		return self.keyword

class Content(models.Model):
	page = models.ForeignKey(Page)
	keyword = models.ForeignKey(Keyword)
	occurrence = models.IntegerField()
	
	def __unicode__(self):
		return self.keyword.keyword + " - " + str(self.occurrence)
