from django.urls import path
from . import views

urlpatterns = [
    path('recetas/', views.RecetasListCreate.as_view(), name='recetas-list'),
    path('recetas/<int:pk>/', views.RecetasDetail.as_view(), name='recetas-detail'),
    path('recetaIngre/', views.RecetaIngreListCreate.as_view(), name='recetaIngre-list'),
    path('recetaIngre/<int:pk>/', views.RecetaIngreDetail.as_view(), name='recetaIngre-detail'),
    path('ingredientes/', views.IngredientesListCreate.as_view(), name='ingredientes-list'),
    path('ingredientes/<int:pk>/', views.IngredientesDetail.as_view(), name='ingredientes-detail'),
    path('categoria/', views.CategoriaListCreate.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('preparacion/', views.PreparacionListCreate.as_view(), name='preparacion-list'),
    path('preparacion/<int:pk>/', views.PreparacionDetail.as_view(), name='preparacion-detail'),
    path('proveedor/', views.ProveedorListCreate.as_view(), name='proveedor-list'),
    path('proveedor/<int:pk>/', views.ProveedorDetail.as_view(), name='proveedor-detail'),

    
]