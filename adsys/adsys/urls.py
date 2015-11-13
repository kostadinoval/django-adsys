from django.conf.urls import patterns, include, url
from django.contrib import admin

'''
Global URL conf file.

Requests are redirected to the specific Django App URLs file which calls the specific view.
'''

urlpatterns = patterns('',
	url(r'^', include('about.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^advert/', include('advert.urls')),
	url(r'^adspace/', include('adspace.urls')),
	url(r'^domain/', include('domain.urls')),
	#url(r'^feedback/', include('feedback.urls')),
	#url(r'^testpage/', include('testpage.urls')),
	url(r'^accounts/', include('registration.backends.simple.urls')),
)
