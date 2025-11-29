# Problema04

class Lista:
    def __init__(self, valores : list, valor_B):
        if len(valores) == 3:
            self.valores = valores
            self.valor_B = valor_B
        else:
            raise ValueError("No cumple con la cantidad de elementos")
        
    def __str__(self):
        return f'lista: {self.valores}'
        
    def __add__(self):
        nuevos_valores = [x + self.valor_B for x in self.valores]
        print(nuevos_valores)
        
    def __sub__(self):
        nuevos_valores = [x - self.valor_B for x in self.valores]
        print(nuevos_valores)
        
    def __mul__(self):
        nuevos_valores = [x * self.valor_B for x in self.valores]
        print(nuevos_valores)
    
    def __truediv__(self):
        nuevos_valores = [x / self.valor_B for x in self.valores]
        print(nuevos_valores)
        
        
        
lista1 = Lista([10, 20, 30], 5)
print(lista1)
print(lista1.__add__())
print(lista1.__sub__())
print(lista1.__mul__())
print(lista1.__truediv__())
 