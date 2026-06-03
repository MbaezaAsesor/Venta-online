from django.contrib import admin
from .models import Categoria, Producto, Opinion

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'activo')
    list_filter = ('categoria', 'activo', 'creado')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'calificacion', 'creado')
    list_filter = ('calificacion', 'creado')