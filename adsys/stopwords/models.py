from django.db import models

class StopWord(models.Model):
	stopword = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.stopword