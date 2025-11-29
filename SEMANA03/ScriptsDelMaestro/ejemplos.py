# 1. Clase de Números
'''Crea una clase Numbers que reciba una lista de números en el constructor. 
Incluye un método squared que use una función lambda para devolver una nueva lista
con los cuadrados de los números, y un método filter_even que devuelva solo los números
pares usando comprensión de listas y condicionales.

'''
class Numbers:
    def __init__(self, nums):
        self.nums = nums
        self.squared = lambda: [x ** 2 for x in self.nums]
        self.filter_even = lambda: [x for x in self.nums if x % 2 == 0]

# Ejemplo de uso
nums = Numbers([1, 2, 3, 4, 5])
print("Cuadrados:", nums.squared())             # [1, 4, 9, 16, 25]
print("Pares:", nums.filter_even())             # [2, 4]





