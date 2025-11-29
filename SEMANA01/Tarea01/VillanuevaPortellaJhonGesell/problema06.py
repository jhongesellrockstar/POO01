"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema06: Escribir una función que reciba una lista de números y devuelva otra lista "
"con solo los números pares usando 'filter' y lambda."

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numeros_pares(lista):
    return list(filter(lambda x: x%2 == 0, lista))

resultado = numeros_pares(numeros)
print("Numeros pares:", resultado)