from django.conf.urls import patterns, include, url
#from django.conf.urls import url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
from django.shortcuts import render, get_object_or_404

admin.autodiscover()

urlpatterns = [

    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^post/about/$', views.post_about, name='post_about'),
    #url(r'^myblog/', include('blog.about')),
]
