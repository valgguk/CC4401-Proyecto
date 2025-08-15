from django import forms
from .models import Peticion
from categorias.models import Item
from django.forms.widgets import DateInput

class PeticionModelForm(forms.ModelForm):
    
    class Meta:
        model = Peticion
        fields = ['titulo', 'tipo', 'descripcion', 'autor', 'estudio', 
                  'director', 'editorial', 'fecha_lanzamiento', 'imagen']
        widgets = {'fecha_lanzamiento': DateInput(attrs={'type': 'date'})}


class ResolverPeticionForm(forms.ModelForm):

    class Meta:
        model = Peticion
        fields = ['estado', 'comentario_admin']

class ItemModelForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['titulo', 'tipo', 'descripcion', 'autor', 'estudio', 
                  'director', 'editorial', 'fecha_lanzamiento', 'imagen']
        widgets = {'fecha_lanzamiento': DateInput(attrs={'type': 'date'})}
		   