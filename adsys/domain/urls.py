from django.conf.urls import patterns, url
from domain import views

'''
Module URLs conf file
'''

urlpatterns = patterns('',
	# Maps to www.example.com/domain/add
	url(r'^add/$', views.add, name='add'),
	
	# Maps to www.example.com/domain/list
	url(r'^list/$', views.list, name='list'),
)