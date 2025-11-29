"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema07: Crear un programa que tenga una lista de nombres de frutas y, mediante "
"un bucle imprima cada fruta en mayúsculas si empieza con la letra 'M'. Puedes usar "
"map con lambda para convertirlas a mayúsculas."


frutas = ["manzana", "pera", "mango", "uva", "melon", "platano"]

frutas_modificadas = list(map(lambda f: f.upper() if f[0].lower() == "m" else f, frutas))

print("Frutas procesadas:")
for fruta in frutas_modificadas:
    print(fruta)