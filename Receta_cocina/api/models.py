from django.db import models

 
class Categoria(models.Model):
    Nombre_Categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"nombre: {self.Nombre_Categoria}"  

    

class Preparacion(models.Model):
    Instrucciones= models.CharField(max_length=100)
    Porciones= models.CharField(max_length=100)
    tiempo_coccion=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" Instruccion: {self.Instrucciones}, porcion: {self.Porciones}, tiempo: {self.tiempo_coccion}" 

class Proveedor(models.Model):
    Nombre_Proveedor= models.CharField(max_length=100)
    Correo= models.CharField(max_length=100)
   
    def __str__(self):
        return f"nombre: {self.Nombre_Proveedor}, correo:{self.Correo}"

class Ingredientes(models.Model):
    Nombre_Ingrediente= models.CharField(max_length=100)
    Proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre_Ingrediente: {self.Nombre_Ingrediente}, proveedor: {self.Proveedor}"

class Recetas(models.Model):
    Nombre_Receta = models.CharField(max_length=100)
    Categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    Preparacion=models.ForeignKey(Preparacion, on_delete=models.CASCADE) 

    def __str__(self):
        return f"nombre: {self.Nombre_Receta}, categoria: {self.Categoria}, preparacion: {self.Preparacion}"
  
  ##tabla intermedia , conecta receta e ingrediente  
class RecetaIngre(models.Model):
    Recetas=models.ForeignKey(Recetas, on_delete=models.CASCADE) 
    Ingredientes=models.ForeignKey(Ingredientes, on_delete=models.CASCADE) 

    def __str__(self):
        return f"receta: {self.Recetas}, ingrediente: {self.Ingredientes}"
    


    

