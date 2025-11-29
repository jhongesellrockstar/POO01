class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self,sueldo):
        self.sueldo = sueldo

empleado1 = Empleado('Juan',25,5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)