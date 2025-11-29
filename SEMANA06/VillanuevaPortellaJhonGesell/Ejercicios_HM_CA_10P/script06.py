from abc import ABC, abstractmethod
import math

# Clase abstracta base
class Forma(ABC):
    def __init__(self, color, linea):
        self.color = color
        self.linea = linea

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def mostrar_detalles(self):
        return f"color={self.color}, linea={self.linea}, area={self.area():.2f}, perimetro={self.perimetro():.2f}"


# Subclase Rectangulo
class Rectangulo(Forma):
    def __init__(self, base, altura, color, linea):
        Forma.__init__(self, color, linea)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar_detalles(self):
        return f"Rectangulo({self.base}x{self.altura}) -> {Forma.mostrar_detalles(self)}"


# Subclase Circulo
class Circulo(Forma):
    def __init__(self, radio, color, linea):
        Forma.__init__(self, color, linea)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_detalles(self):
        return f"Circulo(r={self.radio}) -> {Forma.mostrar_detalles(self)}"


# Subclase Triangulo
class Triangulo(Forma):
    def __init__(self, lado1, lado2, lado3, color, linea):
        Forma.__init__(self, color, linea)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def mostrar_detalles(self):
        return f"Triangulo({self.lado1},{self.lado2},{self.lado3}) -> {Forma.mostrar_detalles(self)}"


# Creación de objetos (sin bloque if)
r = Rectangulo(3, 4, "azul", "continua")
c = Circulo(2, "rojo", "punteada")
t = Triangulo(3, 4, 5, "verde", "continua")

print(r.mostrar_detalles())
print(c.mostrar_detalles())
print(t.mostrar_detalles())
