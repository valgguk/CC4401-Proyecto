from django.urls import path
from . import views


urlpatterns = [
    path('mi-biblioteca/', views.mi_biblioteca, name='mi-biblioteca'),
    path('mi-biblioteca/<str:tipo>/', views.mis_items, name='mis_items'),
    path('mi-biblioteca/<str:tipo>/<int:favorito_id>', views.mi_item, name='mi_item'),
]   