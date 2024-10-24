from django.db import models


# Create your models here.
class Recetas(models.Model):
    Nombre_Receta = models.CharField(max_length=100)
    Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    Preparacion=models.ForeignKey(Preparacion, on_delete=models.CASCADE) 

    def __str__(self):
        return (self.Nombre_Receta)-(self.Categoria)-(self.Preparacion)
  
  ##tabla intermedia , conecta receta e ingrediente  
class RecetaIngre(models.Model):
    Recetas=models.ForeignKey(Recetas, on_delete=models.CASCADE) 
    Ingredientes=models.ForeignKey(Ingredientes, on_delete=models.CASCADE) 

    def __str__(self):
        return (self.Recetas)-(self.Ingredientes)
    
class Ingredientes(models.Model):
    Nombre_Ingrediente= models.DateTimeField(auto_now_add=True)
    Proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)


    def __str__(self):
        return (self.Nombre_Ingrediente)-(self.Proveedor)
 
class Categoria(models.Model):
    Nombre_Categoria = models.CharField(max_length=100)

    def __str__(self):
        return (self.Nombre_Categoria)  

class Preparacion(models.Model):
    Instrucciones= models.CharField(max_length=100)
    Porciones= models.CharField(max_length=100)
    tiempo_coccion=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (self.Instrucciones)-(self.Porciones)-(self.tiempo_coccion) 
    
    
class Proveedor(models.Model):
    Nombre_Proveedor= models.CharField(max_length=100)
    Correo= models.CharField(max_length=100)
   
    def __str__(self):
        return (self.Nombre_Proveedor)-(self.Correo)
