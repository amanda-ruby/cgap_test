from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.participants_form, name='participants_form'),
    path(r'list/', views.participants_list, name='participants_list'),
    path(r'list/review/<int:id>/<str:rev_value>/', views.review_participant, name='review_participant')]