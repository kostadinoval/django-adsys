from django.conf.urls import patterns, url
from testpage import views

urlpatterns = patterns('',
	url(r'^$', views.page, name='page'),
	url(r'^pageA/$', views.pageA, name='pageA'),
    url(r'^pageB/$', views.pageB, name='pageB'),
	url(r'^pageC/$', views.pageC, name='pageC'),
)
