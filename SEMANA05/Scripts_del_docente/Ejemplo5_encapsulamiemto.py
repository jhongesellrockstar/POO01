'''Crear una clase Animal con atributos privados (nombre, edad, especie) 
que representen diferentes animales, utilizando encapsulamiento mediante 
propiedades (getters y setters). Luego, crear una clase hija Perro que herede
de Animal y tenga un método adicional para hacer ladrar.

Se debe definir un diccionario que asocie los nombres de los animales con su
especie. A partir de listas de nombres y edades, y usando este diccionario, crear
objetos Perro (y potencialmente otros animales si se desea) mediante comprensión 
de listas y map con funciones lambda.

Luego, recorrer la lista de animales, mostrar su información con condicionales
dependiendo de su edad (si son jóvenes o adultos), y hacer que cada animal ladre. 
También, transformar los nombres a mayúsculas usando map y lambda, y almacenarlos 
en una lista.'''


# Clase base con encapsulamiento
class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre  # encapsulado
        self.__edad = edad
        self.__especie = especie

    # Getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, valor):
        self.__especie = valor

    def info(self):
        return f"Animal: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad}"

# Clase hija con herencia y método adicional
class Perro(Animal):
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Datos de animales y sus especies usando diccionarios
nombres = ['Fido', 'Rex', 'Luna', 'Max']
edades = [3, 5, 2, 4]
especies = {'Fido': 'Perro', 'Rex': 'Perro', 'Luna': 'Perro', 'Max': 'Perro'}

# Crear objetos Perro usando comprensión y map, incluyendo especie desde diccionario
animales = list(map(lambda n, e: Perro(n, e, especies[n]), nombres, edades))

# Mostrar información con bucles y condicionales
for animal in animales:
    if animal.edad < 4:
        print(animal.info() + " - Es joven.")
    else:
        print(animal.info() + " - Es adulto.")
    print(animal.ladrar())

# Uso de listas map y lambda para obtener nombres en mayúsculas
nombres_mayusculas = list(map(lambda a: a.nombre.upper(), animales))
print("Nombres en mayúsculas:", nombres_mayusculas)
