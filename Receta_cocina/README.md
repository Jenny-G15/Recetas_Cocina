## Nombre del Proyecto: Recetas de Cocina

## Integrantes:
- Jennifer Guadamuz Gómez.
- Maria Laura Morales González.

# API de Recetas con Django

Esta es una API simple creada con Django y Django REST Framework que permite gestionar recetas, ingredientes, categorías, preparaciones y proveedores. Incluye funcionalidades para crear, leer, actualizar y eliminar recetas y sus relaciones con los ingredientes, categorías, y más.

## Índice:
- Tecnologías utilizadas
- Características
- Descripción de Archivos
- Endpoints
- Esquema del proyecto

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- MySQL




## Características

- Crear nuevas recetas, ingredientes, categorías, preparaciones y proveedores.
- Obtener todas las recetas o una receta específica por ID.
- Actualizar recetas, ingredientes, categorías, preparaciones y proveedores existentes.
- Eliminar recetas, ingredientes y relaciones entre ellos.




## Descripción de Archivos

- models.py: Define los modelos de Recetas, Ingredientes, Categorías, Preparaciones y Proveedores, y sus relaciones.

- serializers.py: Contiene los serializadores para transformar los datos de los modelos en JSON y viceversa.

- views.py: Define las vistas basadas en clases para manejar las operaciones CRUD sobre los modelos.

- urls.py: Define las rutas de la API para acceder a las recetas, ingredientes, categorías, y otros modelos.



## Endpoints

- Receta
- Ingredientes
- Categoría
- Preparación
- Proveedor


## Licencia

## Contactenos