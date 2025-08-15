from django import forms
from .models import Tarea
from django.contrib.auth.forms import UserCreationForm
from categorias.models import CustomUser  # tu modelo custom

class TareaForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Tarea
        fields = ['Nombre', 'Username', 'Contraseña', 'Correo']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # los campos que tenga tu CustomUser