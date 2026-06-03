from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('producto/<slug:slug>/', views.ProductoDetailView.as_view(), name='detalle'),
    path('categoria/<slug:slug>/', views.CategoriaView.as_view(), name='categoria'),
]