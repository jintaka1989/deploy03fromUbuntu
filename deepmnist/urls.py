# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^deepmnist/$', views.deepmnist_gui),
    url(r'^deepmnist/new/$', views.deepmnist_new, name='deepmnist_new'),
]
