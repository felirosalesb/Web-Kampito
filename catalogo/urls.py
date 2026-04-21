# catalogo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # La ruta vacía '' es el Home
]