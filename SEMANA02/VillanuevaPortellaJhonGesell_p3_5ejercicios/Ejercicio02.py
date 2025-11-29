"""
Diseñe la clase Persona con los atributos públicos de instancia:
> Nombre (Tipo cadena)
> Apellido (Tipo cadena)
> Edad (Tipo cadena)
> Estatura (Tipo cadena)
> Peso (Tipo real)
Implemente además:
> Un método que retorne el estado de la persona entre: "Menor de edad" o "Mayor de edad".
> Un método que retorne el índice de masa corporal de la persona (peso/altura**2).
En otro archivo:
> Declare y cree un objeto de tipo Persona.
> Ingrese datos fijos.
> Visualice todos sus datos.
"""
class Persona:
    def __init__(self, nombre, apellido, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def estado(self):
        return "Mayor de edad" if self.edad >= 18 else "Menor de edad"

    def indice_masa_corporal(self):
        return self.peso / (self.estatura ** 2)

ejecutar = Persona("Jhon Gesell", "Villanueva Portella", 33, 1.74, 100.0)
print(f"Nombre: {ejecutar.nombre}")
print(f"Apellido: {ejecutar.apellido}")
print(f"Edad: {ejecutar.edad} años")
print(f"Estatura: {ejecutar.estatura} m")
print(f"Peso: {ejecutar.peso} kg")
print(f"Estado: {ejecutar.estado()}")
print(f"Índice de masa corporal: {ejecutar.indice_masa_corporal():.2f}")
