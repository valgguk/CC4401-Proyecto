from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('editar/', views.editar_perfil, name='editar_perfil'),
    path("buscar-usuario/", views.buscar_usuario, name="buscar_usuario"),
    path('<str:username>/seguir/', views.toggle_seguir, name='toggle_seguir'),
    path('<str:username>/', views.perfil_usuario, name='perfil_usuario'),
]
