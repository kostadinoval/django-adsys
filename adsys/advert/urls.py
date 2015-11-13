from django.conf.urls import patterns, url
from advert import views

'''
Module URLs conf file
'''

urlpatterns = patterns('',
	# Maps to www.example.com/advert/list
	url(r'^list/$', views.list, name='list'),
	
	# Maps to www.example.com/advert/create
	url(r'^create/$', views.create, name='create'),
	
	# Maps to www.example.com/advert/view/advert_id
	url(r'^view/(?P<advert_id>\d+)/$', views.view, name='view'),
	
	# Maps to www.example.com/advert/delete/advert_id
	url(r'^delete/(?P<advert_id>\d+)/$', views.delete, name='delete'),
	
	# Maps to www.example.com/advert/edit/advert_id
	url(r'^edit/(?P<advert_id>\d+)/$', views.edit, name='edit'),
	
	# Maps to www.example.com/advert/getAdvert?<<query_string>> AJAX triggered
	url(r'^getAdvert/$', views.getAdvert, name='getAdvert'),
	
	# Maps to www.example.com/advert/getEscaped?data=<<query_string>>
	url(r'^getEscaped/$', views.getEscaped, name='getEscaped'),
)