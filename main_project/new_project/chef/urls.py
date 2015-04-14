from django.conf.urls import patterns, url
from chef import views
from django.shortcuts import render

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about', views.about, name='about'),
                       )