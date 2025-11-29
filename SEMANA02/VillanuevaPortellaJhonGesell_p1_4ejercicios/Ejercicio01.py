"""Implementar una clase llamada Persona que tendrá como atributo (variable) su nombre y dos 
métodos (funciones), uno de dichos métodos inicializara el atributo nombre y el siguiente método 
mostrara en la pantalla el contenido del mismo.
 Definir dos objetos de la clase Persona"""

class Persona:
    def __init__(self):
        # atributo su nombre
        self.nombre = ""

    def inicializar_nombre(self, nombre):
        # Método para asignar un valor
        self.nombre = nombre

    def mostrar_nombre(self):
        print("Nombre:",self.nombre)

p1 = Persona()
p1.inicializar_nombre("Jhon")
p1.mostrar_nombre()

    



        

