"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema04: Crear un programa que pida al usuario una lista de números hasta que ingrese "
"cero. Al finalizar, muestre el promedio de los números ingresando (sin contar el cero). Al "
"finalizar, muestre el promedio de los números ingresados (sin contar el cero). Puedes usar "
"lambda para calcular la suma y el conteo."

numeros = []

while True:
    n = int(input("Ingresa un núnmero (0 para terminar):"))
    if n == 0:
        break
    numeros.append(n)

if numeros:
    suma=(lambda lista: sum(lista))(numeros)
    conteo = (lambda lista: len(lista))(numeros)
    promedio = suma / conteo
    print("El promedio es:", promedio)

else:
    print("No ingresaste ningun número valido.")