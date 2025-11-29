class Animal:
    def hablar(self):
        return "..."


class Perro(Animal):
    def hablar(self):
        return "Guau"


class Gato(Animal):
    def hablar(self):
        return "Miau"


class Pato(Animal):
    def hablar(self):
        return "Cuac"


def hacer_hablar(animales):
    for a in animales:
        print(a.hablar())


zoo = [Perro(), Gato(), Pato(), Gato(), Perro()]
hacer_hablar(zoo)
