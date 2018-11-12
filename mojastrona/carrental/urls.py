# -*- coding: utf-8 -*-
from carrental import views
from carrental.views import AddComment
from django.conf.urls import url, include

app_name='carrental'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mark>\w+)/$', views.cars, name='cars'),
    url(r'^(?P<model>\w+)/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^(?P<model>\w+)/(?P<pk>\d+)/AddComment$', views.AddComment, name='AddComment'),
    url(r'^(?P<model>\w+)/(?P<pk>\d+)/AddToOrder$', views.AddToOrder, name='AddToOrder'),
    url(r'^(?P<model>\w+)/(?P<pk>\d+)/InsurenceEdit$', views.insurenceedit, name='insurenceedit'),
    url(r'^(?P<model>\w+)/(?P<pk>\d+)/OverviewEdit$', views.overviewedit, name='overviewedit'),
]
