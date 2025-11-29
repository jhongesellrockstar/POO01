class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_beneficio(self):
        raise NotImplementedError("Implementar en subclase")

    def __str__(self):
        return f"Empleado({self.nombre})"


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def calcular_beneficio(self):
        return 0.10 * self.sueldo

    def __str__(self):
        return f"EmpleadoFijo({self.nombre}, sueldo={self.sueldo})"


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_beneficio(self):
        return 0.05 * (self.horas * self.tarifa)

    def __str__(self):
        return f"EmpleadoTemporal({self.nombre}, horas={self.horas}, tarifa={self.tarifa})"


class EmpleadoFreelance(Empleado):
    def __init__(self, nombre, proyectos, tarifa_proyecto):
        super().__init__(nombre)
        self.proyectos = proyectos
        self.tarifa_proyecto = tarifa_proyecto

    def calcular_beneficio(self):
        return 0.03 * (self.proyectos * self.tarifa_proyecto)

    def __str__(self):
        return f"EmpleadoFreelance({self.nombre}, proyectos={self.proyectos}, tarifa={self.tarifa_proyecto})"


def mostrar_beneficios(empleados):
    for e in empleados:
        print(f"{e}: beneficio={e.calcular_beneficio():.2f}")


lista_empleados = [
    EmpleadoFijo("Ana", 3000),
    EmpleadoTemporal("Luis", 160, 15),
    EmpleadoFreelance("María", 4, 800)
]
mostrar_beneficios(lista_empleados)
