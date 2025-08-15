from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Reseña
from .forms import ReseñaForm
from django.shortcuts import redirect, get_object_or_404
from .models import Reseña
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required

@login_required
def comentar_reseña(request, reseña_id):
    reseña = get_object_or_404(Reseña, id=reseña_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.reseña = reseña
            comentario.autor = request.user
            comentario.save()
    return redirect('detalle_item', item_id=reseña.item.id)

def detalle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    reseñas = item.reseñas.all()

    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.item = item
            reseña.autor = request.user  # Asegúrate que el usuario esté logueado
            reseña.save()
            return redirect('detalle_item', item_id=item.id)
    else:
        form = ReseñaForm()

    return render(request, 'todoapp/detalle_item.html', {
        'item': item,
        'reseñas': reseñas,
        'form': form
    })