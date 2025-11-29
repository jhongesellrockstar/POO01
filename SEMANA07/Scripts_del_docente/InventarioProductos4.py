'''Problema 2: Inventario de Productos con Operaciones de Búsqueda y Filtrado
Enunciado:
Define una clase Producto con atributos como nombre, categoría, precio y
cantidad en stock.
Crea una lista de objetos Producto.
Implementa funciones para:  

Agregar productos a la lista.
Buscar productos por categoría usando filter y lambda.
Obtener un diccionario con los productos cuyo precio sea menor a 100 usando
comprensión de listas.
Mostrar la lista de productos en stock mayor a 10 unidades.
Realiza estas operaciones en un ciclo, permitiendo ingresar nuevos productos,
consultar información, y presenta resultados en forma ordenada y legible. '''

class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f"Producto: {self.nombre}, Categoría: {self.categoria}, "
                f"Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}")

# Lista de productos
inventario = []

# Agregar algunos productos como ejemplo
inventario.append(Producto("Monitor", "Electrónicos", 150.0, 20))
inventario.append(Producto("Camisa", "Ropa", 35.0, 50))
inventario.append(Producto("Sandwich", "Alimentos", 8.0, 100))
inventario.append(Producto("TV", "Electrónicos", 700.0, 5))
inventario.append(Producto("Pantalón", "Ropa", 45.0, 15))
inventario.append(Producto("Frijoles", "Alimentos", 2.5, 40))

# Buscar productos por categoría
categoria_buscada = "Electrónicos"
productos_categoria = list(filter(lambda p: p.categoria == categoria_buscada, inventario))
print(f"\nProductos en categoría '{categoria_buscada}':")
for p in productos_categoria:
    print(p)

# Crear diccionario con productos con precio menor a 100
productos_baratos = [p for p in inventario if p.precio < 100]
diccionario_productos = {p.nombre: p for p in productos_baratos}
print("\nProductos con precio menor a $100:")
for nombre, prod in diccionario_productos.items():
    print(f"{nombre}: {prod}")

# Mostrar productos con cantidad mayor a 10
productos_stock = list(filter(lambda p: p.cantidad > 10, inventario))
print("\nProductos con stock mayor a 10 unidades:")
for p in productos_stock:
    print(p)
