from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.gender_index),
    path('gender/add', views.gender_create),
    path('gender/store', views.gender_store)
]
