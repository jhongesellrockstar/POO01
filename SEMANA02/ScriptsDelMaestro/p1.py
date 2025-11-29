class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        # Lambda para clasificar la calificación
        self.clasificar = lambda: "Aprobado" if self.calificacion >= 11 else "Desaprobado"

# Crear algunos estudiantes
estudiante1 = Estudiante("Ana", 15)
estudiante2 = Estudiante("Luis", 8)
estudiante3 = Estudiante("Carlos", 11)

# Mostrar si cada estudiante ha aprobado o no usando la lambda
print(f"{estudiante1.nombre} está {estudiante1.clasificar()}")
print(f"{estudiante2.nombre} está {estudiante2.clasificar()}")
print(f"{estudiante3.nombre} está {estudiante3.clasificar()}")