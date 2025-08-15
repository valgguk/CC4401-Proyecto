from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class PerfilUsuario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_usuario')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    seguidores = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='siguiendo_perfiles', blank=True)
