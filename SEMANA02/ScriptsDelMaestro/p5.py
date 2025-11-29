# Definimos una clase para representar productos
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

# Crear una lista de productos
productos = [
    Producto("Manzana", 0.5, "Fruta"),
    Producto("Banana", 0.3, "Fruta"),
    Producto("Leche", 1.2, "Lácteo"),
    Producto("Queso", 2.5, "Lácteo"),
    Producto("Pan", 1.0, "Panadería")
]

# Crear un diccionario con productos filtrados por categoría y precio, usando comprensión de listas
# Solo productos de la categoría "Lácteo" y precio mayor que 1.0
productos_filtrados = {
    p.nombre: p.precio
    for p in productos
    if p.categoria == "Lácteo" and (lambda precio: precio > 1.0)(p.precio)
}

# También, podemos usar un bucle para imprimir los productos filtrados
for nombre, precio in productos_filtrados.items():
    print(f"Producto: {nombre}, Precio: {precio}")
