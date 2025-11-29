class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear objetos de la clase Persona
persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 30)

# Crear una lista que contiene los objetos
personas = [persona1, persona2]

# Obtener una lista de nombres usando comprensión de listas
nombres = [p.nombre for p in personas]
print(nombres)
