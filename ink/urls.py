from django.conf.urls import patterns, url
from ink import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
