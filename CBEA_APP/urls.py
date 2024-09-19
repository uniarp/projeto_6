from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutor_form, name='tutor_form'),  # Mapeia a URL para a view correspondente
    path('', views.animal_form, name='animal_form'),
]