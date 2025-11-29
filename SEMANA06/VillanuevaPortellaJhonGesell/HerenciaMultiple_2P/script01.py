# herencia_multiple_1.py
class FiguraGeometrica:
    def __init__(self, alto=0.0, ancho=0.0):
        self._alto = float(alto)
        self._ancho = float(ancho)

    # get/set alto
    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = float(alto)

    # get/set ancho
    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = float(ancho)

    def __str__(self):
        return f"FiguraGeometrica(alto={self._alto}, ancho={self._ancho})"


class Color:
    def __init__(self, color=""):
        self._color = str(color)

    # get/set color
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = str(color)

    def __str__(self):
        return f"Color({self._color})"


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color=""):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.get_ancho() * self.get_alto()

    def __str__(self):
        return (f"Cuadrado(lado={self.get_ancho()}, color={self.get_color()}, "
                f"area={self.area()})")


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color=""):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.get_ancho() * self.get_alto()

    def __str__(self):
        return (f"Rectangulo(ancho={self.get_ancho()}, alto={self.get_alto()}, "
                f"color={self.get_color()}, area={self.area()})")


print("== Prueba de herencia múltiple (FiguraGeometrica + Color) ==")
c = Cuadrado(lado=5, color="Rojo")
r = Rectangulo(ancho=8, alto=3, color="Azul")
print(c)
print(r)
# Modificando con setters, estilo del diagrama
r.set_alto(4)
r.set_ancho(10)
print("Rectángulo actualizado:", r)
