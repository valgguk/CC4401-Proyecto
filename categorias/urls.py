from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:item_id>/', views.detalle_item, name='detalle_item'),
    path('reseña/<int:reseña_id>/comentar/', views.comentar_reseña, name='comentar_reseña'),
]