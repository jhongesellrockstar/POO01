# Paso 1: Lista de números del 1 al 100
numeros = list(range(1, 101))

# Paso 2: Crear la lista de diccionarios para números pares
info_pares = [
    {
        'numero': n,
        'cuadrado': n ** 2,
        'es_multiplo_de_4': n % 4 == 0,
        'categoria': (
            'bajo' if n <= 33 else
            'medio' if n <= 66 else
            'alto'
        )
    }
    for n in numeros if n % 2 == 0
]

# Paso 3: Filtrar e imprimir según condiciones
print("Diccionarios con múltiplos de 4 y categoría 'medio' o 'alto':\n")
for item in info_pares:
    if item['es_multiplo_de_4'] and item['categoria'] in ['medio', 'alto']:
        print(item)
