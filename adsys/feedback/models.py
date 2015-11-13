from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
	user = models.ForeignKey(User, null = True, blank = True)
	email = models.EmailField(max_length=254)
	type = models.CharField(max_length=20)
	comment = models.TextField()
	datetime_posted = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return str(self.pk) + " - " +self.type