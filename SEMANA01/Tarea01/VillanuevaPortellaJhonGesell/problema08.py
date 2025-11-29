"POO-01, estudiante VILLANUEVA PORTELLA JHON GESELL"

"Problema08: Definir una función que reciba un diccionario con productos y sus precios, "
"y devuelva el total de todos los precios usando map y sum. También se puede usar lambda "
"para extraer precios."

def total_precios(productos):
    return sum(map(lambda x: x, productos.values()))

productos = {
    "Arroz": 5.50,
    "Leche": 3.20,
    "Pan": 2.00,
    "Huevos": 8.70,
    "Pan de hamburgueza": 8.00,
    "Harina": 3.50,
    "Mantequilla": 2.50,

}

resultado = total_precios(productos)
print("El total de los precios es: ", resultado)