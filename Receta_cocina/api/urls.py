from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoListCreate.as_view(), name='producto-list'),
    path('productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),
    path('cliente/', views.ClienteListCreate.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),
    path('pedido/', views.PedidoListCreate.as_view(), name='pedido-list'),
    path('pedido/<int:pk>/', views.PedidoDetail.as_view(), name='pedido-detail'),
    path('venta/', views.VentaListCreate.as_view(), name='venta-list'),
    path('venta/<int:pk>/', views.VentaDetail.as_view(), name='venta-detail'),
    
]