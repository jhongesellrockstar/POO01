class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self.__nombre = nombre
        self.__precio = 0.0
        self.__cantidad = int(cantidad)
        self.set_precio(precio)  # usa el setter para validar

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        # doble control: numérico y no negativo
        try:
            p = float(nuevo_precio)
        except:
            print("precio inválido (no numérico)")
            return
        if p < 0:
            print("precio inválido (negativo)")
            return
        self.__precio = p

    def get_cantidad(self):
        return self.__cantidad

    def aumentar_stock(self, unidades):
        if unidades <= 0:
            print("unidades inválidas para aumentar")
            return
        self.__cantidad = self.__cantidad + int(unidades)

    def reducir_stock(self, unidades):
        if unidades <= 0:
            print("unidades inválidas para reducir")
            return
        if unidades > self.__cantidad:
            print("stock insuficiente")
            return
        self.__cantidad = self.__cantidad - int(unidades)

    def mostrar(self):
        print("producto:", self.__nombre, "| precio:", self.__precio, "| stock:", self.__cantidad)

# Pruebas
p = Producto("Mouse USB", 39.9, 10)
p.mostrar()

p.aumentar_stock(5)
p.mostrar()

p.reducir_stock(12)
p.mostrar()

p.set_precio(-20)   # rechazado
p.set_precio("abc") # rechazado
p.set_precio(42.5)  # aceptado
p.mostrar()