# Clase base: Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Nombre: {self.nombre}"

# Clase Cliente hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, dinero):
        super().__init__(nombre)
        self.dinero = dinero
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)

    def total_compra(self):
        return sum(map(lambda p: p.precio, self.carrito))

    def pagar(self):
        total = self.total_compra()
        if self.dinero >= total:
            self.dinero -= total
            return True
        return False

    def __str__(self):
        productos = ', '.join([p.nombre for p in self.carrito])
        return f"{super().__str__()}, Dinero: ${self.dinero:.2f}, Carrito: [{productos}]"

# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

# Clase Vendedor hereda de Persona
class Vendedor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.ventas = []

    def procesar_venta(self, cliente):
        if cliente.pagar():
            self.ventas.extend(cliente.carrito)
            print(f"✅ Venta realizada a {cliente.nombre}. Total: ${cliente.total_compra():.2f}")
            cliente.carrito.clear()
        else:
            print(f"❌ {cliente.nombre} no tiene suficiente dinero para pagar.")

    def __str__(self):
        total_ventas = sum(p.precio for p in self.ventas)
        return f"{super().__str__()}, Ventas totales: ${total_ventas:.2f}"

# --- Simulación ---

# Crear productos
inventario = [
    Producto("Laptop", 1200),
    Producto("Mouse", 25),
    Producto("Teclado", 45),
    Producto("Monitor", 300)
]

# Crear cliente y vendedor
cliente = Cliente("Ana", 1000)
vendedor = Vendedor("Carlos")

# Cliente agrega productos al carrito usando un bucle
for producto in inventario:
    if producto.precio <= 500:  # Condición: sólo productos más baratos
        cliente.agregar_producto(producto)

print("\n🛍️ Estado antes de la compra:")
print(cliente)
print(vendedor)

# Vendedor procesa la venta
vendedor.procesar_venta(cliente)

print("\n🧾 Estado después de la compra:")
print(cliente)
print(vendedor)
