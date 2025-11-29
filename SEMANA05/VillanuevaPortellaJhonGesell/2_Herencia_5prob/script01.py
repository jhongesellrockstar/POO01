class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    # Getters (acceso controlado)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad


class Perro(Animal):
    def ladrar(self):
        return f"{self.get_nombre()} ladra: Guau"


class Gato(Animal):
    def maullar(self):
        return f"{self.get_nombre()} maúlla: Miau"


p = Perro("Almendra", 4)
g = Gato("Mía", 3)

print(p.info(), "|", p.ladrar())
print(g.info(), "|", g.maullar())
