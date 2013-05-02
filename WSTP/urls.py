from django.conf.urls import patterns, include, url
from test.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',index),
    url(r'^intro/([\w.-]+)/$',intro),
    url(r'^content/([\w.-]+)/$',content_default,name="content"),
    url(r'^content/([\w.-]+)/([\w.-]+)/$',content),
    url(r'^register/$',register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^check/username/$',check_username),
    url(r'^check/email/$',check_email)
    # url(r'^$', 'WSTP.views.home', name='home'),
    # url(r'^WSTP/', include('WSTP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)