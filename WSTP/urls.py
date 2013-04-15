from django.conf.urls import patterns, include, url
from test.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',index),
    url(r'^sql_injiection_intro/$',sql_injiection_intro),
    url(r'^mysql/$',mysql),
    # url(r'^$', 'WSTP.views.home', name='home'),
    # url(r'^WSTP/', include('WSTP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)