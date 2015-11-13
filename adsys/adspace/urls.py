from django.conf.urls import patterns, url
from adspace import views

'''
Module URLs conf file
'''

urlpatterns = patterns('',
	
	# Maps to www.example.com/adspace/list
	url(r'^list/$', views.list, name='list'),
	
	# Maps to www.example.com/adspace/create
	url(r'^create/$', views.create, name='create'),
	
	# Maps to www.example.com/adspace/view/adspace_id
	url(r'^view/(?P<adspace_id>\d+)/$', views.view, name='view'),
	
	# Maps to www.example.com/adspace/delete/adspace_id
	url(r'^delete/(?P<adspace_id>\d+)/$', views.delete, name='delete'),
)