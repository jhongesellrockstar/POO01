from abc import ABC, abstractmethod

# Clase abstracta Trabajador
class Trabajador(ABC):
    
    @abstractmethod
    def calcular_pago(self):
        pass

# Clase TrabajadorPorHora que hereda de Trabajador
class TrabajadorPorHora(Trabajador):
    
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Clase TrabajadorFijo que hereda de Trabajador
class TrabajadorFijo(Trabajador):
    
    def __init__(self, salario_fijo):
        self.salario_fijo = salario_fijo
    
    def calcular_pago(self):
        return self.salario_fijo

# Clase TrabajadorFreelance que hereda de Trabajador
class TrabajadorFreelance(Trabajador):
    
    def __init__(self, proyectos_completados, tarifa_por_proyecto):
        self.proyectos_completados = proyectos_completados
        self.tarifa_por_proyecto = tarifa_por_proyecto
    
    def calcular_pago(self):
        return self.proyectos_completados * self.tarifa_por_proyecto

# Pruebas
trabajador_hora = TrabajadorPorHora(40, 20)
print(f"Pago del trabajador por hora: {trabajador_hora.calcular_pago()}")  # Salida: 800

trabajador_fijo = TrabajadorFijo(2500)
print(f"Pago del trabajador fijo: {trabajador_fijo.calcular_pago()}")  # Salida: 2500

trabajador_freelance = TrabajadorFreelance(5, 300)
print(f"Pago del trabajador freelance: {trabajador_freelance.calcular_pago()}")  # Salida: 1500
