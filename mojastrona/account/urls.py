# -*- coding: utf-8 -*-
from account import views
from django.conf.urls import url, include

app_name='account'
urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                       {'template_name': 'registration/logged_out.html'},
                       name = 'logout',),
    url(r'^logout_then_login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^editfault/(?P<pk>\d+)$', views.editfault, name='EditFault'),
    url(r'^addcfault/(?P<pk>\d+)$', views.AddFaultComment, name='AddCFault'),   
]
