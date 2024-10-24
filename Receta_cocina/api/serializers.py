from rest_framework import serializers
from .models import Recetas
from .models import RecetaIngre
from .models import Ingredientes
from .models import Categoria
from .models import Preparacion
from .models import Proveedor

class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = '__all__'
        
    def validate(self, data):
            if data['Nombre' and 'Categoria' and 'Preparacion'] is None:
                raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
            return data
        
class RecetaIngreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngre
        fields = '__all__'
    
    def validate(self, data):
            if data['Recetas' and 'Ingredientes'] is None:
                raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
            return data

    
    

        
class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'
    
    def validate(self, data):
        if data['Nombre_Ingrediente' and 'Proveedor'] is None:
            raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
        return data




class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    def validate(self, data):
        if data['Nombre_Categoria'] is None:
            raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
        return data
    
        
        

class PreparacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparacion
        fields = '__all__'
    
    def validate(self, data):
        if data['Instrucciones' and 'Porciones' and 'tiempo_coccion'] is None:
            raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
        return data
        
        

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

    def validate(self, data):
        if data['Nombre_Proveedor' and 'Correo'] is None:
            raise serializers.ValidationError("¡Error!, no pueden haber especios vacios.")
        return data