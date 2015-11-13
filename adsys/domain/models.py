from django.db import models
from django.contrib.auth.models import User

class Domain(models.Model):
	user = models.ForeignKey(User)
	domain = models.URLField()
	crawled = models.BooleanField(default=False)
	datetime_posted = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.domain
