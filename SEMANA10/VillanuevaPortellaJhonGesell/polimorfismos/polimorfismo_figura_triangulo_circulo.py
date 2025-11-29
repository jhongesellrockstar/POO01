import math

class Figura:
    def perimetro(self):
        raise NotImplementedError("Implementar en subclase")

    def area(self):
        raise NotImplementedError("Implementar en subclase")


class Triangulo(Figura):
    def __init__(self):
        self.lado_01 = float(input("Ingrese el lado 1 del triángulo: "))
        self.lado_02 = float(input("Ingrese el lado 2 del triángulo: "))
        self.lado_03 = float(input("Ingrese el lado 3 del triángulo: "))

    def perimetro(self):
        return self.lado_01 + self.lado_02 + self.lado_03

    def area(self):
        p = self.perimetro() / 2
        return math.sqrt(p * (p - self.lado_01) * (p - self.lado_02) * (p - self.lado_03))

    def __str__(self):
        return (f"Triángulo → lados: {self.lado_01}, {self.lado_02}, {self.lado_03} | "
                f"Perímetro: {self.perimetro():.2f} | Área: {self.area():.2f}")


class Circulo(Figura):
    def __init__(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return (f"Círculo → radio: {self.radio} | "
                f"Perímetro: {self.perimetro():.2f} | Área: {self.area():.2f}")


def mostrar_datos(figuras):
    for f in figuras:
        print(f)


triangulo = Triangulo()
circulo = Circulo()
figuras = [triangulo, circulo]
mostrar_datos(figuras)
