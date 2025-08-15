from django.shortcuts import render, redirect
from peticiones.forms import PeticionModelForm, ResolverPeticionForm, ItemModelForm
from .models import Peticion
from categorias.models import Item


def peticiones(request):
    if request.method == "GET":
        form_peticion = PeticionModelForm()
        return render(request, "peticiones/peticion-base.html", {"form_peticion": form_peticion, "listo": False})

    if request.method == "POST":
        form_peticion = PeticionModelForm(request.POST)
        if form_peticion.is_valid():
            nueva_peticion = form_peticion.save()
            return render(request, "peticiones/peticion-base.html", {"form_peticion": form_peticion, "listo": True})
        else:
            # Mostrar el formulario con errores
            return render(request, "peticiones/peticion-base.html", {"form_peticion": form_peticion, "listo": False})
        
def ver_peticiones(request):
    peticiones_db = Peticion.objects.all()
    if request.method  == 'GET':
        return render(request, 'peticiones/ver-peticiones.html', {"peticiones": peticiones_db})
    else:
        return ""

def resolver_peticion(request, peticion_id):
    peticion = Peticion.objects.get(id= peticion_id)
    if request.method  == 'GET':
        form_resolver = ResolverPeticionForm()
        return render(request, 'peticiones/resolver-peticion.html', {"peticion": peticion, "form_resolver": form_resolver})
    if request.method == "POST":
        form_resolver = ResolverPeticionForm(request.POST, instance=peticion)
        if form_resolver.is_valid():
            nueva_resolucion = form_resolver.save()
            if nueva_resolucion.estado == 'ACEPTADO':
                # Verificar si ya se creó un Libro para evitar duplicados
                    Item.objects.create(
                        titulo=nueva_resolucion.titulo,
                        descripcion=nueva_resolucion.descripcion,
                        tipo=nueva_resolucion.tipo,
                        autor=nueva_resolucion.autor,
                        estudio=nueva_resolucion.estudio,
                        director=nueva_resolucion.director,
                        editorial=nueva_resolucion.editorial,
                        fecha_lanzamiento=nueva_resolucion.fecha_lanzamiento,
                        imagen=nueva_resolucion.imagen
                    )
            return redirect('peticiones:ver-peticiones')
        else:
            # Mostrar el formulario con errores
            return render(request, "peticiones/peticion-base.html", {"peticion": peticion, "form_resolver": form_resolver})

def agregar_item(request):
    if request.method == "GET":
        form_item = ItemModelForm()
        return render(request, "peticiones/agregar-item.html", {"form_item": form_item, "listo": False})

    if request.method == "POST":
        form_item = ItemModelForm(request.POST)
        if form_item.is_valid():
            nuevo_item = form_item.save()
            return render(request, "peticiones/agregar-item.html", {"form_item": form_item, "listo": True})
        else:
            # Mostrar el formulario con errores
            return render(request, "peticiones/agregar-item.html", {"form_item": form_item, "listo": False})