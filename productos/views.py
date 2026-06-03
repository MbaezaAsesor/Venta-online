from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Producto, Categoria

class InicioView(ListView):
    model = Producto
    template_name = 'productos/inicio.html'
    context_object_name = 'productos'
    paginate_by = 12

    def get_queryset(self):
        return Producto.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/detalle.html'
    context_object_name = 'producto'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opiniones'] = self.object.opiniones.all()
        context['productos_relacionados'] = Producto.objects.filter(
            categoria=self.object.categoria,
            activo=True
        ).exclude(id=self.object.id)[:4]
        return context


class CategoriaView(ListView):
    model = Producto
    template_name = 'productos/categoria.html'
    context_object_name = 'productos'
    paginate_by = 12

    def get_queryset(self):
        slug = self.kwargs['slug']
        categoria = get_object_or_404(Categoria, slug=slug)
        return Producto.objects.filter(categoria=categoria, activo=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_actual'] = Categoria.objects.get(slug=self.kwargs['slug'])
        return context