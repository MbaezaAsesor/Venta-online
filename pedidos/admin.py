from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['producto']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_pedido', 'usuario', 'estado', 'total', 'creado')
    list_filter = ('estado', 'creado')
    search_fields = ('numero_pedido', 'usuario__username')
    inlines = [ItemPedidoInline]