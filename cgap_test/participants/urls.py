from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.participants_form, name='participants_form'),
    path(r'list/', views.participants_list, name='participants_list'),
]