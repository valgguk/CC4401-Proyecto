from django.urls import path
from . import views

app_name = 'peticiones'

urlpatterns = [
    path('peticiones/', views.peticiones, name='peticion-base'),
    path('ver-peticiones/', views.ver_peticiones, name='ver-peticiones'),
    path('ver-peticiones/<int:peticion_id>/', views.resolver_peticion, name='resolver_peticion'),
    path('agregar_item/', views.agregar_item, name='agregar_item'),
]     