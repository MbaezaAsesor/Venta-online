from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pedido

@login_required
def carrito(request):
    carrito = request.session.get('carrito', {})
    return render(request, 'pedidos/carrito.html', {'carrito': carrito})


class MisPedidosView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'pedidos/mis_pedidos.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)


class PedidoDetailView(LoginRequiredMixin, DetailView):
    model = Pedido
    template_name = 'pedidos/detalle_pedido.html'
    context_object_name = 'pedido'

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user)