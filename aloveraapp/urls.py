from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.gender_index),
    path('gender/add', views.gender_create),
    path('gender/store', views.gender_store),
    path('gender/edit/<int:gender_id>', views.gender_edit),
    path('gender/update/<int:gender_id>', views.gender_update),
    path('gender/delete/<int:gender_id>', views.gender_delete),
    path('gender/destroy/<int:gender_id>', views.gender_destroy)
]
