"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"problema02: Escribir un programa que tenga un diccionario con nombres "
"de estudiantes y sus edades. Mostrar los nombres de los estudiantes "
"que tienen más de 18 años usando 'filter' y una función lambda."

estudiantes = {
    "Ana": 17,
    "Pedro": 16,
    "Fiorella": 24,
    "Jhon": 23,
    "Ker": 21,
    "Jimmy": 20
}

mayores = list(filter(lambda nombre: estudiantes[nombre] > 18, estudiantes))

print("Estudiantes mayores de 18 años:")
for nombre in mayores:
    print(nombre)

