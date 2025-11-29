class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    

class Perro(Animal):
    def ladrar(self):
        return f'{self.nombre} dice GUAU'

# Creas un Perro con parámetros
perro = Perro("Fido", 3)  # Esto funciona
print(perro.ladrar())
