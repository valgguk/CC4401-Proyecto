from django import forms
from .models import Reseña, Comentario

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['contenido']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
