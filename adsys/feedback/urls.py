from django.conf.urls import patterns, url
from feedback import views

'''
Module URLs conf file
'''

urlpatterns = patterns('',
	# Maps to www.example.com/feedback
	url(r'^$', views.post, name='post'),
)