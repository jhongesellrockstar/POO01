class Producto:
    total_productos = 0

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        Producto.total_productos += cantidad

    def eliminar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            Producto.total_productos -= cantidad
        else:
            print("No hay suficientes productos para eliminar.")

# Crear productos
p1 = Producto("Laptops", 10)
p2 = Producto("Tabletas", 5)

# Eliminar algunos productos
p1.eliminar(2)

# Mostrar el total de productos en el inventario
print(f"Total de productos en inventario: {Producto.total_productos}")
