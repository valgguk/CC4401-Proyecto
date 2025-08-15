from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
"""" 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    """

# Modelo de Usuario personalizado (opcional)
# la tabla de usuario ya está integrada por Django, pero podemos añadirle más cositas
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrador'),
        ('usuario', 'Usuario común'),
    )
    tipo = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='usuario')

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    biblioteca = models.ManyToManyField('Item', through='Favorito')

    seguidores = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='siguiendo_usuarios',
        blank=True
    )
    
    def __str__(self):
        return self.username
    
# Un test simple para mostrar atributos básicos, despues usaré la definida
# Para insertar facil a la base de datos:

# py manage.py shell
# >> from categorias.models import Libro_test
# >> Libro_test.objects.create(titulo="<nombre_libro>")
# >> quit()

class Libro_test(models.Model):
    titulo = models.CharField(max_length=200)

    
# Modelo general de "Item" (libros, animes, mangas, películas, cómics)
class Item(models.Model):
    TIPO_CHOICES = [
        ('Libro', 'Libro'),
        ('Manga', 'Manga'),
        ('Anime', 'Anime'),
        ('Película', 'Película'),
        ('Cómic', 'Cómic'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    autor = models.CharField(max_length=100, null=True, blank=True)
    estudio = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    editorial = models.CharField(max_length=100, null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.URLField(blank=True)
    def __str__(self):
        return f"{self.titulo} ({self.tipo})"
    

# Reseña de un ítem por un usuario
class Reseña(models.Model):
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reseñas')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reseñas')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='reseñas_likeadas')

    def __str__(self):
        return f"Reseña de {self.item.titulo} por {self.autor.username}"
    

# Comentario dentro de una reseña
class Comentario(models.Model):
    reseña = models.ForeignKey(Reseña, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentario de {self.autor.username} en reseña #{self.reseña.id}"


class Favorito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    puntuacion = models.PositiveSmallIntegerField(blank=True, validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], null=True)
    marca_pagina = models.TextField(blank=True)