"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema09: Pedir al usuario que ingrese varias edades. Al finalizar, determinar cuantas"
"edades son mayores de 20 usando filter y lambda."

edades = []
while True:
    n = int(input("Ingresa una edad (0 para terminar):"))
    if n == 0:
        break
    edades.append(n)

mayores_20 = list(filter(lambda x: x > 20, edades))

print("Cantidad de edades mayores de 20:", len(mayores_20))