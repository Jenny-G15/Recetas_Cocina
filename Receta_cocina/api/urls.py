from django.urls import path
from . import views

urlpatterns = [
    path('recetas/', views.RecetasListCreate.as_view(), name='receta-list'),
    path('recetas/<int:pk>/', views.RecetasDetail.as_view(), name='producto-detail'),
    
]