from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, tipo_combustible, velocidad=0):
        self.tipo_combustible = tipo_combustible.lower()
        self.velocidad = velocidad

    @abstractmethod
    def acelerar(self, incremento):
        pass

    @abstractmethod
    def frenar(self, decremento):
        pass

    def estado(self):
        return f"{self.__class__.__name__} | combustible={self.tipo_combustible} | v={self.velocidad} km/h"


# Subclase Auto
class Auto(Vehiculo):
    COMBUSTIBLES_PERMITIDOS = {"gasolina", "diesel", "eléctrico", "híbrido"}

    def acelerar(self, incremento):
        if self.tipo_combustible not in Auto.COMBUSTIBLES_PERMITIDOS:
            print("Combustible no compatible para Auto")
            return
        self.velocidad += incremento
        print(f"Acelera Auto a {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"Frena Auto a {self.velocidad} km/h")


# Subclase Motocicleta
class Motocicleta(Vehiculo):
    COMBUSTIBLES_PERMITIDOS = {"gasolina", "eléctrico"}

    def acelerar(self, incremento):
        if self.tipo_combustible not in Motocicleta.COMBUSTIBLES_PERMITIDOS:
            print("Combustible no compatible para Motocicleta")
            return
        self.velocidad += incremento
        print(f"Acelera Motocicleta a {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"Frena Motocicleta a {self.velocidad} km/h")


# Ejemplo de uso (sin if __main__)
a = Auto("híbrido")
print(a.acelerar(30))
print(a.frenar(10))
print(a.estado())

m = Motocicleta("eléctrico")
print(m.acelerar(20))
print(m.frenar(5))
print(m.estado())
