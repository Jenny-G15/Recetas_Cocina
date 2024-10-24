from rest_framework import generics
from .models import Recetas 
from .models import RecetaIngre 
from .models import Ingredientes
from .models import Categoria 
from .models import Preparacion 
from .models import Proveedor
from .serializers import RecetasSerializer
from .serializers import RecetaIngreSerializer 
from .serializers import IngredientesSerializer 
from .serializers import CategoriaSerializer
from .serializers import PreparacionSerializer 
from .serializers import ProveedorSerializer

# Recetas
class RecetasListCreate(generics.ListCreateAPIView):
    queryset = Recetas.objects.all()
    serializer_class = RecetasSerializer

class RecetasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recetas.objects.all()
    serializer_class = RecetasSerializer




# RecetaIngre (tabla intermedia)
class RecetaIngreListCreate(generics.ListCreateAPIView):
    queryset = RecetaIngre.objects.all()
    serializer_class = RecetaIngreSerializer

class RecetaIngreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecetaIngre.objects.all()
    serializer_class = RecetaIngreSerializer



# Ingredientes
class IngredientesListCreate(generics.ListCreateAPIView):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer

class IngredientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer



# Categoría
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



# Preparación

class PreparacionListCreate(generics.ListCreateAPIView):
    queryset = Preparacion.objects.all()
    serializer_class = PreparacionSerializer

class PreparacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Preparacion.objects.all()
    serializer_class = PreparacionSerializer



# Proveedor

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
