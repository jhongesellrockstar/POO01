"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema03: Definir una función que tome una lista de palabras y devuelva una lista con "
"las palabras que empiezan con la letra 'A' (mayúsculas o minúscula) usando 'filter' y lambda."

palabras = ["Alburquerque", "casa", "argon", "Sol", "Agua", "Montaña", "avión", "arroyo", "ADCP"]



def palabras_con_a(lista):
    return list(filter(lambda palabra: palabra[0].lower() == 'a', lista))


resultado = palabras_con_a(palabras)

print("Palabras que empiezan con 'A':", resultado)