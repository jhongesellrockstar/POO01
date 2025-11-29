"""
Diseñe la clase Numeros con los atributos publicos:
> Numero1 (Tipo entero)
> Numero2 (Tipo entero)
> Numero3 (Tipo entero)
Implemente además los siguientes métodos:
> Un método que retorne el número menor.
> Un método que retorne el número mayor.
> Un método que retorne el número del medio (ubicado entre el menor y el mayor)
Tomando la clase números:
> Declare y cree un objeto de tipo Números
> Ingrese datos fijos
> Visualice todos sus datos
"""
class Numeros:
    def __init__(self, Numero1, Numero2, Numero3):
        self.Numero1 = Numero1
        self.Numero2 = Numero2
        self.Numero3 = Numero3

    def numero_menor(self):
        return min(self.Numero1, self.Numero2, self.Numero3)

    def numero_mayor(self):
        return max(self.Numero1, self.Numero2, self.Numero3)

    def numero_medio(self):
        lista = [self.Numero1, self.Numero2, self.Numero3]
        lista.sort()
        return lista[1]  # El número del medio después de ordenar

    def mostrar_datos(self):
        print("Número 1:", self.Numero1)
        print("Número 2:", self.Numero2)
        print("Número 3:", self.Numero3)
        print("Número menor:", self.numero_menor())
        print("Número mayor:", self.numero_mayor())
        print("Número del medio:", self.numero_medio())



Ejecutar = Numeros(1, 2, 3)
Ejecutar.mostrar_datos()
