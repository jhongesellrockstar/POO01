# script01.py  (corregido)
class Vehiculo:
    def __init__(self, nombre, marca, modelo, velocidad_maxima):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def info(self):
        return f"{self.nombre} | {self.marca} {self.modelo} | vmax={self.velocidad_maxima} km/h"


class VehiculoAcuatico(Vehiculo):
    def __init__(self, nombre, marca, modelo, velocidad_maxima, profundidad_maxima):
        # Llamada directa a la clase base para evitar conflicto con MRO
        Vehiculo.__init__(self, nombre, marca, modelo, velocidad_maxima)
        self.profundidad_maxima = profundidad_maxima

    def navegar(self):
        return f"{self.nombre} navegando (profundidad máx {self.profundidad_maxima} m)"


class VehiculoAereo(Vehiculo):
    def __init__(self, nombre, marca, modelo, velocidad_maxima, altura_maxima):
        Vehiculo.__init__(self, nombre, marca, modelo, velocidad_maxima)
        self.altura_maxima = altura_maxima

    def volar(self):
        return f"{self.nombre} volando (altura máx {self.altura_maxima} m)"


class VehiculoHibrido(VehiculoAcuatico, VehiculoAereo):
    def __init__(self, nombre, marca, modelo, velocidad_maxima,
                 profundidad_maxima, altura_maxima, capacidad_combustible):
        VehiculoAcuatico.__init__(self, nombre, marca, modelo, velocidad_maxima, profundidad_maxima)
        VehiculoAereo.__init__(self, nombre, marca, modelo, velocidad_maxima, altura_maxima)
        self.capacidad_combustible = capacidad_combustible

    def capacidades(self):
        return f"{self.navegar()} y también {self.volar()}"

    def info(self):
        base = Vehiculo.info(self)
        return f"{base} | tanque={self.capacidad_combustible} L"


# --- Prueba principal ---
h = VehiculoHibrido("Hydra-1", "NeoTech", "HX", 320, 200, 6000, 800)
print(h.info())
print(h.navegar())
print(h.volar())
print(h.capacidades())
