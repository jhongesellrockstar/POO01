class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

        # Método lambda para calcular el precio con descuento
        self.calcular_precio_final = lambda: self.precio - (self.precio * self.descuento / 100)
        
        # Método lambda para verificar si el descuento es válido
        self.descuento_valido = lambda: "Válido" if 0 <= self.descuento <= 50 else "Inválido"

    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        precio_final = self.calcular_precio_final()
        descuento_valido = self.descuento_valido()
        print(f"Producto: {self.nombre}")
        print(f"Precio Original: ${self.precio}")
        print(f"Precio con Descuento: ${precio_final}")
        print(f"Descuento: {self.descuento}% ({descuento_valido})")
        print("-" * 30)

# Crear 3 productos sin almacenarlos en listas
producto1 = Producto("Laptop", 1200, 10)
producto2 = Producto("Teléfono", 800, 5)
producto3 = Producto("Tablet", 500, 55)  # Descuento inválido

# Mostrar la información de cada producto individualmente
producto1.mostrar_informacion()
producto2.mostrar_informacion()
producto3.mostrar_informacion()