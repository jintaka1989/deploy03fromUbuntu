# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^$', views.post_list),
    #名前をつけて、htmlで名前でurl指定したらエラーが出なくなった
    url(r'(?P<post_id>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail),
]
