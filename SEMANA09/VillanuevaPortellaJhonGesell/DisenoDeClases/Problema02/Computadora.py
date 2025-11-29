from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor: Monitor, teclado: Teclado, raton: Raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return (f"Computadora[id={self.idComputadora}, nombre={self.nombre}, "
                f"monitor={self.monitor}, teclado={self.teclado}, raton={self.raton}]")
