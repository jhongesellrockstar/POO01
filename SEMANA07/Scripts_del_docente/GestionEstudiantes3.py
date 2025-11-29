'''Problema 1: Sistema de Gestión de Estudiantes y Calificaciones
Enunciado:
Crea una clase Estudiante que tenga atributos como nombre, edad y un diccionario
de calificaciones (materia: nota).
Implementa funciones para:  

Agregar nombres y edades de estudiantes.
Registrar calificaciones por materia.
obtener la lista de estudiantes mayores de 18 años con promedio superior a 7 
en todas sus materias.
Utiliza listas, comprensiones, filter y lambda para generar la lista filtrada 
y calcular promedios.
Al finalizar, imprime los datos de los estudiantes filtrados de forma clara.'''

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = {}  # materia: nota

    def agregar_calificacion(self, materia, nota):
        self.calificaciones[materia] = nota

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio():.2f}"

# Crear lista de estudiantes
estudiantes = []

# Agregar algunos estudiantes como ejemplo
est1 = Estudiante("Luis", 20)
est1.agregar_calificacion("Matemáticas", 8)
est1.agregar_calificacion("Historia", 7)
#print(f'{est1.calificaciones}')

est2 = Estudiante("Ana", 17)
est2.agregar_calificacion("Matemáticas", 6)
est2.agregar_calificacion("Historia", 5)

est3 = Estudiante("Carlos", 22)
est3.agregar_calificacion("Matemáticas", 9)
est3.agregar_calificacion("Historia", 8)

estudiantes.extend([est1, est2, est3])

# Filtrar estudiantes mayores de 18 con promedio > 7
filtrados = list(filter(lambda e: e.edad > 18 and e.promedio() > 7, estudiantes))

# Mostrar resultados
for e in filtrados:
    print(e)
