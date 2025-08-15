from django.urls import include, path
from django.contrib.auth import views as auth_views
from todoapp import views
from .views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_tarea, name='crear_tarea'),  
    path('usuarios_list/', views.lista_usuarios, name='lista_usuarios'),  
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('libros/', view_libros_list, name='view_libros_list'),
    path('mangas/', view_mangas_list, name='view_mangas_list'),
    path('animes/', view_animes_list, name='view_animes_list'),
    path('peliculas/', view_peliculas_list, name='view_peliculas_list'),
    path('comics/', view_comics_list, name='view_comics_list'),
    path('usuarios/', include('usuarios.urls')),
    path('registro/', views.registro_usuario, name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar/<int:item_id>/', views.agregar_item, name='agregar-item'),
    path('buscar_item/', views.buscar_item, name='buscar_item'),
    path('bibliotecas/', views.biblioteca_global, name='biblioteca_global'),
]
