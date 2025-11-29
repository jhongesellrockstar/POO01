# script05.py
class Animal:
    def __init__(self, nombre, energia=100):
        self.nombre = nombre
        self.energia = energia

class Volador:
    def __init__(self, altura_max):
        self.altura_max = altura_max

    def volar(self, metros):
        if metros <= self.altura_max:
            return f"{self.nombre} vuela {metros} m."
        return f"{self.nombre} no puede superar {self.altura_max} m."

class Nadador:
    def __init__(self, profundidad_max):
        self.profundidad_max = profundidad_max

    def nadar(self, metros):
        if metros <= self.profundidad_max:
            return f"{self.nombre} nada {metros} m."
        return f"{self.nombre} no puede superar {self.profundidad_max} m de profundidad."

class PinguinoVoladorNadador(Animal, Volador, Nadador):
    def __init__(self, nombre, altura_max, profundidad_max):
        Animal.__init__(self, nombre, energia=80)
        Volador.__init__(self, altura_max)
        Nadador.__init__(self, profundidad_max)

    def estado(self):
        return f"{self.nombre} | energía={self.energia} | alt máx={self.altura_max} | prof máx={self.profundidad_max}"

p = PinguinoVoladorNadador("Pingo", altura_max=5, profundidad_max=50)
print(p.estado())
print(p.volar(4))
print(p.nadar(40))
