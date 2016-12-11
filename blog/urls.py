#from django.conf.urls import patterns, include, url
from django.conf.urls import url
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
from . import views
from django.shortcuts import render, get_object_or_404

#admin.autodiscover()

urlpatterns = [

    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
