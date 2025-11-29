# herencia_multiple_2.py
class Producto:
    def __init__(self, cantidad=0, costo=0.0):
        self._cantidad = int(cantidad)
        self._costo = float(costo)

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = int(cantidad)

    def get_costo(self):
        return self._costo

    def set_costo(self, costo):
        self._costo = float(costo)

    def calculo_total(self):
        return self._cantidad * self._costo

    def __str__(self):
        return f"Producto(cantidad={self._cantidad}, costo={self._costo:.2f})"


class Fruta:
    def __init__(self, nombre="", origen=""):
        self._nombre = str(nombre)
        self._origen = str(origen)

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = str(nombre)

    def get_origen(self):
        return self._origen

    def set_origen(self, origen):
        self._origen = str(origen)

    def __str__(self):
        return f"Fruta(nombre={self._nombre}, origen={self._origen})"


class Articulo(Producto, Fruta):
    def __init__(self, nombre, origen, cantidad, costo):
        Producto.__init__(self, cantidad=cantidad, costo=costo)
        Fruta.__init__(self, nombre=nombre, origen=origen)

    def __str__(self):
        # Formato de salida inspirado en la lámina
        lineas = [
            f"La fruta es {self.get_nombre()}",
            f"Con origen en {self.get_origen()}",
            f"Se tienen {self.get_cantidad()} productos",
            f"El costo del producto es $ {self.get_costo():.2f}",
            f"Se tiene en total $ {self.calculo_total():.2f}",
        ]
        return "\n".join(lineas)


articulo = Articulo(nombre="Manzana", origen="México", cantidad=500, costo=10.56)
print(articulo)
