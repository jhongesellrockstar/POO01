# script09.py
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, emp_id, sueldo_base=0):
        self.nombre = nombre
        self.emp_id = emp_id
        self.sueldo_base = sueldo_base

    @abstractmethod
    def calcular_sueldo(self): ...

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, emp_id, sueldo_base, bonos=0):
        super().__init__(nombre, emp_id, sueldo_base)
        self.bonos = bonos
    def calcular_sueldo(self):
        return self.sueldo_base + self.bonos

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, emp_id, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, emp_id, 0)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    def calcular_sueldo(self):
        return self.horas_trabajadas * self.tarifa_por_hora

e1 = EmpleadoTiempoCompleto("Ana", 1, 2500, bonos=500)
e2 = EmpleadoPorHoras("Luis", 2, horas_trabajadas=120, tarifa_por_hora=15)
print(f"{e1.nombre}: S/. {e1.calcular_sueldo():.2f}")
print(f"{e2.nombre}: S/. {e2.calcular_sueldo():.2f}")
