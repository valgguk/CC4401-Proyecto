from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from categorias.models import CustomUser
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def seguir_usuario(request, username):
    objetivo = get_object_or_404(CustomUser, username=username)
    if objetivo != request.user:
        if objetivo in request.user.siguiendo.all():
            request.user.siguiendo.remove(objetivo)
        else:
            request.user.siguiendo.add(objetivo)
    return redirect('ver_perfil', username=objetivo.username)

@login_required
def perfil_usuario(request, username):
    usuario = get_object_or_404(CustomUser, username=username)
    es_mi_perfil = request.user == usuario
    siguiendo = request.user.siguiendo_usuarios.all() if es_mi_perfil else None

    return render(request, 'usuarios/perfil_usuario.html', {
        'usuario_perfil': usuario,
        'es_mi_perfil': es_mi_perfil,
        'siguiendo': siguiendo
    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def editar_perfil(request):
    usuario = request.user
    mensaje_confirmacion = None

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('first_name')
        nuevo_apellido = request.POST.get('last_name')
        nuevo_email = request.POST.get('email')
        nueva_bio = request.POST.get('bio')

        if 'avatar' in request.FILES:
            usuario.avatar = request.FILES['avatar']

        usuario.first_name = nuevo_nombre
        usuario.last_name = nuevo_apellido
        usuario.email = nuevo_email
        usuario.bio = nueva_bio
        usuario.save()

        mensaje_confirmacion = "Cambios guardados correctamente."

    return render(request, 'usuarios/editar_perfil.html', {
        'username': usuario.username,
        'first_name': usuario.first_name,
        'last_name': usuario.last_name,
        'email': usuario.email,
        'bio': usuario.bio,
        'mensaje_confirmacion': mensaje_confirmacion,
    })



@require_POST
@login_required
def toggle_seguir(request, username):
    objetivo = get_object_or_404(CustomUser, username=username)
    if objetivo != request.user:
        if objetivo in request.user.siguiendo_usuarios.all():
            request.user.siguiendo_usuarios.remove(objetivo)
        else:
            request.user.siguiendo_usuarios.add(objetivo)
    return HttpResponseRedirect(reverse('usuarios:perfil_usuario', args=[username]))

from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

@login_required
def buscar_usuario(request):
    query = request.GET.get("q2")
    resultados = []
    if query:
        resultados = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    return render(request, "usuarios/resultados_busqueda.html", {"usuarios": resultados, "query": query})
