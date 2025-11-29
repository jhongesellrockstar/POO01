"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema10: Crear una función que reciba una lista de números y un valor N, y "
"devuelva cuantos números en la lista son mayores que N usando filter y lambda."

def mayores_que(lista, N):
    return len(list(filter(lambda x: x>N, lista)))

numeros = [3,7,10,57,15,2,20,25]
N=10
resultado = mayores_que(numeros,N)

print(f"Cantidad de números mayores que {N}: {resultado}")