from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cabelo', views.cabelo, name='cabelo'),
    path('barba', views.barba, name='barba'),
    path('informacoes', views.informacoes, name='informacoes')
]
