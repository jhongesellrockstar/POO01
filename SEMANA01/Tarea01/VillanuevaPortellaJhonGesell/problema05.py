"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema05: Tener un diccionario con nombres de países y sus capitales. Preguntar "
"al usuario un nombre de país y mostrar su capital si está en el diccionario, o un "
"mensaje de error si no. Aquí se puede hacer con una función lambda para devolver "
"la capital."


paises = {
    "Perú": "Lima",
    "Chile": "Santiago",
    "Argentina": "Brasil",
    "Colombia": "Bógota",
    "España": "Madrid",
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "Rusia": "Moscú",
    
}

pais = input("Ingrese el nombre de un país: ")

capital = (lambda p: paises[p] if p in paises else None) (pais)

if capital:
    print(f"La capital de {pais} es {capital}.")

else:
    print("El pais no esta en el diccionario")