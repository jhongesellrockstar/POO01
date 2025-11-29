class Figura:
    def area(self):
        raise NotImplementedError("Implementar en subclase")

    def perimetro(self):
        raise NotImplementedError("Implementar en subclase")


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1415926535 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.1415926535 * self.radio

    def __str__(self):
        return f"Circulo(r={self.radio})"


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def __str__(self):
        return f"Rectangulo({self.ancho}x{self.alto})"


class Triangulo(Figura):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimetro(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangulo(a={self.a}, b={self.b}, c={self.c})"


def mostrar_figuras(figuras):
    for f in figuras:
        print(f"{f}: area={f.area():.2f}, perimetro={f.perimetro():.2f}")


figs = [Circulo(3), Rectangulo(4, 6), Triangulo(3, 4, 5)]
mostrar_figuras(figs)
