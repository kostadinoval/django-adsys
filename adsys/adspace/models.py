from django.db import models
from django.contrib.auth.models import User

class AdSpace(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=80)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	border_colour = models.CharField(max_length=7, default="#000000")
	adspace_code = models.TextField(default="")
	datetime_posted = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title