"""
Crea una clase Estudiante con atributos nombre, edad y notas (una lista de números).
Luego crea una lista de 3 estudiantes y muestra el nombre de aquellos cuya nota promedio sea mayor o igual a 14.
"""
class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)
estudiantes = [
    Estudiante("Ana", 20, [15, 14, 16]),
    Estudiante("Luis", 22, [12, 13, 11]),
    Estudiante("Marta", 21, [14, 15, 14])
]
for estudiante in estudiantes:
    if estudiante.promedio() >= 14:
        print(f"Nombre: {estudiante.nombre}, Promedio: {estudiante.promedio():.2f}")










