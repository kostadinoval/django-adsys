from django.conf.urls import patterns, url
from about import views
'''

Module URLs conf file

'''
urlpatterns = patterns('',
	
	# Maps to www.example.com
	url(r'^$', views.about, name='about'),
	
	# Maps to www.example.com/faq
	url(r'^faq/$', views.faq, name='faq'),
)