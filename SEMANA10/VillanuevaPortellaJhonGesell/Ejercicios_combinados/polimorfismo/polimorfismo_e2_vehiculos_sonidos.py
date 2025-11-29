class Vehiculo:
    def sonido(self):
        return "..."


class Coche(Vehiculo):
    def sonido(self):
        return "Vroom"


class Moto(Vehiculo):
    def sonido(self):
        return "Brrr"


class Camion(Vehiculo):
    def sonido(self):
        return "Rrrr"


def reproducir_sonidos(vehiculos):
    for v in vehiculos:
        print(v.sonido())


vehiculos = [Coche(), Moto(), Camion(), Coche()]
reproducir_sonidos(vehiculos)
