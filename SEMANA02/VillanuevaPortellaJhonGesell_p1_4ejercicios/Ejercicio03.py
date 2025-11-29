""" Confeccionar una clase que permita cargar el nombre y la edad de una persona. Mostrar los datos 
cargados. Imprimir un mensaje si es mayor de edad (edad>=18)"""


class PersonaEdad:
    def __init__(self):
        self.nombre = ""
        self.edad = 0

    def cargar(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def mostrar(self):
        print("Nombre ", self.nombre, " Edad ", self.edad)

    def mayor_de_edad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor de edad")

pe = PersonaEdad()
pe.cargar()
pe.mostrar()
pe.mayor_de_edad()




