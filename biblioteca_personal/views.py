from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from categorias.models import Item, CustomUser, Favorito

@login_required
def mi_biblioteca(request):
    return render(request, 'biblioteca_personal/biblioteca.html')

@login_required
def mis_items(request, tipo):
    user = request.user
    favoritos = Favorito.objects.filter(usuario=user, item__tipo=tipo)
    biblioteca = favoritos if favoritos.exists() else None
    # bool para indicar si se aplicó filtro o no, sirve para controlar lo que se muestra en el html en caso de no encontrar nada con filtros 
    aplica_filtro = False

    if biblioteca:  
        # Obtener los inputs del filtro
        titulo = request.GET.get('titulo')
        autor = request.GET.get('autor')
        editorial = request.GET.get('editorial')    # None si se esta viendo mis Animes, Peliculas
        estudio = request.GET.get('estudio')        # None si se esta viendo Libros, Mangas, Comics
        director = request.GET.get('director')      # None si se esta viendo Libros, Mangas, Comics
        fecha = request.GET.get('fecha_lanzamiento')
        orden = request.GET.get('orden_puntuacion', '')

        # Revisar que filtros se aplicaron
        if titulo: 
            biblioteca = biblioteca.filter(item__titulo__icontains=titulo)
            aplica_filtro = True

        if autor:
            biblioteca = biblioteca.filter(item__autor__icontains=autor)
            aplica_filtro = True

        if editorial:
            biblioteca = biblioteca.filter(item__editorial__icontains=editorial)
            aplica_filtro = True

        if estudio:
            biblioteca = biblioteca.filter(item__estudio__icontains=estudio)
            aplica_filtro = True

        if director:
            biblioteca = biblioteca.filter(item__director__icontains=director)
            aplica_filtro = True
        
        if fecha:
            biblioteca = biblioteca.filter(item__fecha_lanzamiento=fecha)
            aplica_filtro = True

        if orden == "ascendente":
            biblioteca = biblioteca.order_by('puntuacion')
        elif orden == "descendente":
            biblioteca = biblioteca.order_by('-puntuacion')
        
        # Los 'algo'_actual es para no perder informacion del input del usuario al aplicar filtros
        return render(request, 'biblioteca_personal/mi-biblio.html', 
                  {'biblioteca': biblioteca,
                    'tipo': tipo,
                    'aplica_filtro': aplica_filtro,
                    'titulo_actual': titulo,
                    'autor_actual': autor,
                    'editorial_actual': editorial,
                    'estudio_actual': estudio,
                    'director_actual': director,
                    'fecha_lanzamiento_actual': fecha,
                    'orden_puntuacion': orden,
                    })
    else: 
        return render(request, 'biblioteca_personal/mi-biblio.html', {'biblioteca': biblioteca, 'tipo': tipo, 'aplica_filtro': aplica_filtro})

@login_required
def mi_item(request, tipo, favorito_id):
    favorito = get_object_or_404(Favorito, id=favorito_id, usuario=request.user)
    if request.method == 'POST':
        marca_pagina = request.POST.get('marca_pagina')
        puntuacion = request.POST.get('puntuacion')
        if puntuacion:
            favorito.puntuacion = int(puntuacion)

        favorito.marca_pagina = marca_pagina
        favorito.save()
        return redirect(request.path)
    return render(request, 'biblioteca_personal/mi-item.html', {'favorito': favorito, 'tipo': tipo})




