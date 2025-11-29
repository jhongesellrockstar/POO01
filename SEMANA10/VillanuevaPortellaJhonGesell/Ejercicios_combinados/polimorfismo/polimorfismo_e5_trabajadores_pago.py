class Trabajador:
    def calcular_pago(self):
        raise NotImplementedError("Implementar en subclase")


class TrabajadorPorHora(Trabajador):
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa

    def __str__(self):
        return f"TrabajadorPorHora(horas={self.horas}, tarifa={self.tarifa})"


class TrabajadorPorProyecto(Trabajador):
    def __init__(self, proyectos, tarifa_proyecto):
        self.proyectos = proyectos
        self.tarifa_proyecto = tarifa_proyecto

    def calcular_pago(self):
        return self.proyectos * self.tarifa_proyecto

    def __str__(self):
        return f"TrabajadorPorProyecto(proyectos={self.proyectos}, tarifa={self.tarifa_proyecto})"


def mostrar_pagos(trabajadores):
    for t in trabajadores:
        print(f"{t}: pago={t.calcular_pago():.2f}")


planilla = [
    TrabajadorPorHora(40, 12.5),
    TrabajadorPorProyecto(3, 700),
    TrabajadorPorHora(20, 15.0)
]
mostrar_pagos(planilla)
