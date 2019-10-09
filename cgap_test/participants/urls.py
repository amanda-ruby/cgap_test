from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.participants_form, name='participants_form')
]