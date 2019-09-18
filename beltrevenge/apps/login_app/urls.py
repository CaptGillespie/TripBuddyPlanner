from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup),
    url(r'^createUser$', views.createUser),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]