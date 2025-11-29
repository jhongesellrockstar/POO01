"""Desarrollar un programa que cargue los datos de un triangulo por teclado e implemente los 
siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que 
muestre si es equilatero o no. El nombre de la clase llamarla triangulo"""
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor_lado(self):
        lista = [self.lado1, self.lado2, self.lado3]
        mayor_tamanio = max(lista)
        print("El tamaño de mayor lado mide: ", mayor_tamanio)

    def equilatero(self):
        if self.lado1 == self.lado2:
            if self.lado2 == self.lado3:
                print("Es un triangulo equilatero")

print("Traingulo caso 01")
ejecutar1 = Triangulo(3,4,5)
ejecutar1.mayor_lado()
ejecutar1.equilatero()

print("Traingulo caso 02")
ejecutar2 = Triangulo(3,3,3)
ejecutar2.mayor_lado()
ejecutar2.equilatero()
