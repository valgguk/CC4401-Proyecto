from django.shortcuts import render, redirect, get_object_or_404
from categorias.models import *
from .models import Tarea
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import TareaForm
from .forms import CustomUserCreationForm
from django.urls import reverse

@login_required
def inicio(request):
    return render(request, 'inicio.html')

def crear_tarea(request):
    # post = Envía información al servidor, cuando usuario hace guardar, hace post a http...
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            # donde lo redirigimos
            return redirect('crear_tarea')
    else:  #GET = Pide información. (cuando ingresamos, hace Get a http.. )
        form = TareaForm()
    return render(request, 'todoapp/crear_tarea.html', {'form': form})

def lista_usuarios(request):
    tareas = Tarea.objects.all()
    return render(request, 'todoapp/lista_usuarios.html', {'tareas': tareas})


def view_libros_list(request):
    libros_db = Item.objects.filter(tipo='Libro')

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    editorial = request.GET.get('editorial')
    fecha = request.GET.get('fecha_lanzamiento')
    descripcion = request.GET.get('descripcion')

    favs = Favorito.objects.filter(usuario= request.user).values_list('item_id', flat=True)

    if titulo: 
        libros_db = libros_db.filter(titulo__icontains=titulo)
    if autor:
        libros_db = libros_db.filter(autor__icontains=autor)
    if editorial:
        libros_db = libros_db.filter(editorial__icontains=editorial)
    if fecha:
        libros_db = libros_db.filter(fecha_lanzamiento=fecha)
    if descripcion:
        libros_db = libros_db.filter(descripcion__icontains=descripcion)
    
    context = {
        "libros": libros_db,
        "titulo_actual": titulo,
        "autor_actual": autor,
        "editorial_actual": editorial,
        "fecha_actual": fecha,
        "descripcion_actual": descripcion,
        "favs": favs,
    }

    return render(request, 'todoapp/view_libros_list.html', context)
    
def view_mangas_list(request):
    mangas_db = Item.objects.filter(tipo='Manga')

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    editorial = request.GET.get('editorial')
    fecha = request.GET.get('fecha_lanzamiento')
    descripcion = request.GET.get('descripcion')

    favs = Favorito.objects.filter(usuario= request.user).values_list('item_id', flat=True)

    if titulo:
        mangas_db = mangas_db.filter(titulo__icontains=titulo)
    if autor:
        mangas_db = mangas_db.filter(autor__icontains=autor)
    if editorial:
        mangas_db = mangas_db.filter(editorial__icontains=editorial)
    if fecha:
        mangas_db = mangas_db.filter(fecha_lanzamiento=fecha)
    if descripcion:
        mangas_db = mangas_db.filter(descripcion__icontains=descripcion)
    
    context = {
        "mangas": mangas_db,
        "titulo_actual": titulo,
        "autor_actual": autor,
        "editorial_actual": editorial,
        "fecha_actual": fecha,
        "descripcion_actual": descripcion,
        "favs": favs,
    }

    return render(request, 'todoapp/view_mangas_list.html', context)

def view_animes_list(request):
    animes_db = Item.objects.filter(tipo='Anime')

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    estudio = request.GET.get('estudio')
    director = request.GET.get('director')
    fecha = request.GET.get('fecha_lanzamiento')
    descripcion = request.GET.get('descripcion')

    favs = Favorito.objects.filter(usuario= request.user).values_list('item_id', flat=True)

    if titulo:
        animes_db = animes_db.filter(titulo__icontains=titulo)
    if autor:
        animes_db = animes_db.filter(autor__icontains=autor)
    if estudio:
        animes_db = animes_db.filter(estudio__icontains=estudio)
    if director:
        animes_db = animes_db.filter(director__icontains=director)
    if fecha:
        animes_db = animes_db.filter(fecha_lanzamiento=fecha)
    if descripcion:
        animes_db = animes_db.filter(descripcion__icontains=descripcion)
    
    context = {
        "animes": animes_db,
        "titulo_actual": titulo,
        "autor_actual": autor,
        "estudio_actual": estudio,
        "director_actual": director,
        "fecha_actual": fecha,
        "descripcion_actual": descripcion,
        "favs": favs,
    }

    return render(request, 'todoapp/view_animes_list.html', context)

def view_peliculas_list(request):
    peliculas_db = Item.objects.filter(tipo='Película')

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    estudio = request.GET.get('estudio')
    director = request.GET.get('director')
    fecha = request.GET.get('fecha_lanzamiento')
    descripcion = request.GET.get('descripcion')

    favs = Favorito.objects.filter(usuario= request.user).values_list('item_id', flat=True)

    if titulo:
        peliculas_db = peliculas_db.filter(titulo__icontains=titulo)
    if autor:
        peliculas_db = peliculas_db.filter(autor__icontains=autor)
    if estudio:
        peliculas_db = peliculas_db.filter(estudio__icontains=estudio)
    if director:
        peliculas_db = peliculas_db.filter(director__icontains=director)
    if fecha:
        peliculas_db = peliculas_db.filter(fecha_lanzamiento=fecha)
    if descripcion:
        peliculas_db = peliculas_db.filter(descripcion__icontains=descripcion)
    
    context = {
        "peliculas": peliculas_db,
        "titulo_actual": titulo,
        "autor_actual": autor,
        "estudio_actual": estudio,
        "director_actual": director,
        "fecha_actual": fecha,
        "descripcion_actual": descripcion,
        "favs": favs,
    }

    return render(request, 'todoapp/view_peliculas_list.html', context)
    
def view_comics_list(request):
    comics_db = Item.objects.filter(tipo='Cómic')

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    editorial = request.GET.get('editorial')
    fecha = request.GET.get('fecha_lanzamiento')
    descripcion = request.GET.get('descripcion')

    favs = Favorito.objects.filter(usuario= request.user).values_list('item_id', flat=True)

    if titulo:
        comics_db = comics_db.filter(titulo__icontains=titulo)
    if autor:
        comics_db = comics_db.filter(autor__icontains=autor)
    if editorial:
        comics_db = comics_db.filter(editorial__icontains=editorial)
    if fecha:
        comics_db = comics_db.filter(fecha_lanzamiento=fecha)
    if descripcion:
        comics_db = comics_db.filter(descripcion__icontains=descripcion)
    
    context = {
        "comics": comics_db,
        "titulo_actual": titulo,
        "autor_actual": autor,
        "editorial_actual": editorial,
        "fecha_actual": fecha,
        "descripcion_actual": descripcion,
        "favs": favs,
    }

    return render(request, 'todoapp/view_comics_list.html', context)



def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada correctamente.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def agregar_item(request, item_id):
    if request.method == 'POST':
        user = request.user
        item = get_object_or_404(Item, id=item_id)
        puntuacion = int(request.POST.get('puntuacion'))
        marca_pagina = request.POST.get('marca_pagina')
        favorito, creado = Favorito.objects.get_or_create(usuario=user, item=item, 
                                                          marca_pagina=marca_pagina, puntuacion= puntuacion)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
def buscar_item(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        query_params = f"?titulo={titulo}"
        if tipo == 'Manga':
            url = reverse('view_mangas_list')
        elif tipo == 'Anime':
            url = reverse('view_animes_list')
        elif tipo == 'Cómic':
            url = reverse('view_comics_list')
        elif tipo == 'Película':
            url = reverse('view_peliculas_list')
        elif tipo == 'Libro':
            url = reverse('view_libros_list')
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        return redirect(url + query_params)
    
def biblioteca_global(request):
    return render(request, 'todoapp/biblioteca_global.html')