# Clase base
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


# Subclase para empleados por hora
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_salario(self):
        if self.horas < 0 or self.tarifa < 0:
            raise ValueError("Horas y tarifa deben ser valores positivos")
        return self.horas * self.tarifa


# Subclase para empleados por comisión
class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas, comision):
        super().__init__(nombre)
        self.ventas = ventas
        self.comision = comision

    def calcular_salario(self):
        if self.ventas < 0 or self.comision < 0:
            raise ValueError("Ventas y comisión deben ser valores positivos")
        return self.ventas * self.comision


# Lista de empleados (algunos con errores para probar excepciones)
empleados = [
    EmpleadoPorHora("Luis", 40, 15),
    EmpleadoPorComision("Ana", 5000, 0.05),
    EmpleadoPorHora("Carlos", -5, 12),           # Error: horas negativas
    EmpleadoPorComision("María", 3000, -0.03)     # Error: comisión negativa
]

# Función que calcula salario con manejo de excepciones
def calcular_salario_seguro(empleado):
    try:
        salario = empleado.calcular_salario()
        return f"{empleado.nombre}: S/ {salario:.2f}"
    except Exception as e:
        return f"{empleado.nombre}: Error → {e}"

# Uso de map y lambda para aplicar la función a cada empleado
resultados = list(map(lambda emp: calcular_salario_seguro(emp), empleados))

# Mostrar resultados finales
print("Resultados del cálculo de salarios:")
for resultado in resultados:
    print("-", resultado)
