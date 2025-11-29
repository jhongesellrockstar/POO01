"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema01: Crear una función que reciba una lista de números y retorne "
"la suma de sus elementos usando 'reduce' y una función lambda."

lista = [2, 4, 6, 8, 10]

from functools import reduce
def suma_lista(numeros):
    return reduce(lambda x, y: x + y, numeros)

resultado = suma_lista(lista)
print("La suma es: ", resultado)