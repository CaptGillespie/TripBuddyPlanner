from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^new$', views.new),
    url(r'^createtrip$', views.createtrip),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^updatetrip/(?P<id>\d+)$', views.updatetrip),
    url(r'^join/(?P<id>\d+)$', views.join),
]