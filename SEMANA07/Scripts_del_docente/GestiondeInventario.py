'''Eres responsable de un sistema para gestionar un inventario de productos
en una tienda. Cada producto tiene un nombre, categoría, cantidad en stock
y precio unitario. Además, quieres soportar operaciones fáciles para agregar 
y quitar productos, filtrar productos por criterios, y realizar transacciones 
de compra y venta.

Requisitos:  

Define una clase Producto con atributos: nombre, categoria, cantidad, precio. Incluye métodos para mostrar los datos (__str__) y operator overloading para la suma (__add__) y resta (__sub__) de cantidades de productos.

Crea una lista de objetos Producto con al menos 5 productos de diferentes categorías y precios.

Convierte esa lista en un diccionario usando comprensión de listas donde las claves sean los nombres de los productos y los valores los objetos Producto.

Implementa funciones para:

Agregar productos al inventario (uso de __add__ si quieres manipular cantidades de productos iguales).
Quitar productos del inventario (usando __sub__).
Filtrar productos que tengan un precio menor a 50 usando filter() y lambda.
Obtener una lista de productos en stock con cantidad mayor a 10 usando comprensión de listas.
Simula una venta y una compra:

La venta reduce la cantidad de un producto si hay suficiente stock.
La compra incrementa la cantidad del producto.
Muestra los estados de productos antes y después de las transacciones.
Finalmente, calcula y muestra:

El total del inventario sumando todos los precios de productos multiplicados por sus cantidades.
La lista de productos filtrados por precio.
La diferencia en stock usando sobrecarga de operadores __add__ y __sub__.'''

# Clase Producto con sobrecarga de operadores y método __str__
class Producto:
    def __init__(self, nombre, categoria, cantidad, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return (f"Producto: {self.nombre}, Categoría: {self.categoria}, "
                f"Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}")

    def __add__(self, cantidad):
        # Suma la cantidad a la stock
        if isinstance(cantidad, int):
            return Producto(self.nombre, self.categoria, self.cantidad + cantidad, self.precio)
        return self

    def __sub__(self, cantidad):
        # Resta la cantidad a la stock
        if isinstance(cantidad, int):
            nueva_cantidad = self.cantidad - cantidad
            if nueva_cantidad < 0:
                print("Cantidad insuficiente para la venta o retiro.")
                return self
            return Producto(self.nombre, self.categoria, nueva_cantidad, self.precio)
        return self

# Crear lista de productos
inventario = [
    Producto("Monitor", "Electrónicos", 20, 150.0),
    Producto("Camisa", "Ropa", 50, 35.0),
    Producto("Sandwich", "Alimentos", 100, 8.0),
    Producto("TV", "Electrónicos", 5, 700.0),
    Producto("Pantalón", "Ropa", 15, 45.0)
]

# Convertir en diccionario usando comprensión de diccionarios
inventario_dict = {p.nombre: p for p in inventario}

# Función para mostrar inventario
def mostrar_inventario(lista):
    for p in lista:
        print(p)

print("Inventario inicial:")
mostrar_inventario(inventario)
print()

# Filtrar productos con precio menor a 50 usando filter y lambda
productos_baratos = list(filter(lambda p: p.precio < 50, inventario))
print("Productos con precio menor a $50:")
mostrar_inventario(productos_baratos)
print()

# Lista de productos con cantidad mayor a 10 usando comprensión de listas
productos_stock_mayor_10 = [p for p in inventario if p.cantidad > 10]
print("Productos en stock mayor a 10 unidades:")
mostrar_inventario(productos_stock_mayor_10)
print()

# Simular una venta: vender 5 unidades del TV (si hay suficiente stock)
producto_tv = inventario_dict["TV"]
print("Estado del TV antes de vender 3 unidades:")
print(producto_tv,'\n')
producto_tv = producto_tv - 3  # venta de 3 unidades
print("Estado del TV después de vender 3 unidades:")
print(producto_tv,'\n')
print()

# Simular una compra: aumentar en 10 unidades la camiseta
producto_camisa = inventario_dict["Camisa"]
print("Estado de la Camisa antes de comprar 10 unidades:")
print(producto_camisa)
producto_camisa = producto_camisa + 10
print("Estado de la Camisa después de comprar 10 unidades:")
print(producto_camisa)
print()

# Mostrar el inventario actualizado
print("Inventario después de transacciones:")
mostrar_inventario([
    producto_tv,
    producto_camisa,
    inventario_dict["Monitor"],
    inventario_dict["Sandwich"],
    inventario_dict["Pantalón"]
])

# Calcular el total del inventario
total_inventario = sum(p.cantidad * p.precio for p in inventario)
print(f"\nEl valor total del inventario es: ${total_inventario:.2f}")
