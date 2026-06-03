from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('mis-pedidos/', views.MisPedidosView.as_view(), name='mis_pedidos'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='detalle'),
]