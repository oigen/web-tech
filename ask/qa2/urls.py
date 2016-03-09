from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns ('',
 	
	url(r'^$', 'test', name='index'),
	url(r'^login/', 'test', name='login'),
	url(r'^signup/$', 'qa.views.test'),
	url(r'^question/\d+/$', 'qa.views.test'),	
	url(r'^ask/$', 'qa.views.test'),
	url(r'^popular/$', 'qa.views.test'),
	url(r'^new/$', 'qa.views.test'),
)
