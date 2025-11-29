class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado:
    def __init__(self, salario, cargo):
        self.salario = salario
        self.cargo = cargo

# Clase que hereda de Persona y Empleado
class Ingeniero(Persona, Empleado):
    def __init__(self, nombre, edad, salario, cargo, especialidad):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, salario, cargo)
        self.especialidad = especialidad

    def mostrar_info(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, "
                f"Salario: {self.salario}, Cargo: {self.cargo}, "
                f"Especialidad: {self.especialidad}")

# Uso
juan = Ingeniero("Juan Pérez", 30, 5000, "Jefe de Proyecto", "Software")
print(juan.mostrar_info())
