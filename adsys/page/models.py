from django.db import models
from domain.models import Domain

class Page(models.Model):
	domain = models.ForeignKey(Domain)
	pageURL = models.URLField()
	has_adscore = models.BooleanField(default=False)
	text = models.TextField(default="")
	crawl_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.pageURL