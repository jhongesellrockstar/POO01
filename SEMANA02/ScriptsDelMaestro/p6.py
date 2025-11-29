class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

# Crear lista de estudiantes
estudiantes = [
    Estudiante("Ana", 20, [15, 14, 16]),
    Estudiante("Luis", 21, [10, 12, 11]),
    Estudiante("María", 22, [17, 18, 19])
]

# Mostrar estudiantes con promedio >= 14
print("Estudiantes con buen promedio:")
for est in estudiantes:
    if est.promedio() >= 14:
        print(f"- {est.nombre} (Promedio: {est.promedio():.2f})")
