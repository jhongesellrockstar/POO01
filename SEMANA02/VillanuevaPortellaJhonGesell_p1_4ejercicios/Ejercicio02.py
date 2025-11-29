"""Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los  
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si esta aprobado (nota 
mayor o igual a 11)
 Definir dos objetos de la clase alumno"""
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        # muestra nombre del alumno y su nota
        print("nombre: ", self.nombre, ", Nota:", self.nota)
    
    def esta_aprobado(self):
        if self.nota >= 11:
            print("Aprobado")
        else:
            print("Desaprobado")

a1 = Alumno("Jhon", 15)
a1.imprimir()
a1.esta_aprobado()
        



