"""
a. Crea una lista con los números del 1 al 100.
b. Usando comprensión de listas, crea una nueva lista que contenga un diccionario por cada número par, con la siguiente estructura:
    {
         'número': <número>,
         'cuadrado': <número al cuadrado>,
         'es_multiplo_de_4':<True/False>
         'categoria': <"bajo", "medio", "alto">
    }
    La categoría se asigna según el valor del número:
        - "bajo" si el número esta entre 1 y 33
        - "medio" si esta entre 34 y 66
        - "alto" si está entre 67 y 100
c. Imprime solo los diccionarios donde es_multiplo_de_4 sea True y la categoría sea "medio" o "alto".
"""
# a. Crear lista con números del 1 al 100
numeros = list(range(1, 101))

# b. Crear lista de diccionarios SOLO con números pares
diccionarios = [
    {
        'número': n,
        'cuadrado': n ** 2,
        'es_multiplo_de_4': n % 4 == 0,
        'categoria': (
            "bajo" if 1 <= n <= 33 else
            "medio" if 34 <= n <= 66 else
            "alto"
        )
    }
    for n in numeros if n % 2 == 0
]

# c. Filtrar: múltiplos de 4 y categoría "medio" o "alto"
for d in diccionarios:
    es_multiplo = d['es_multiplo_de_4']        # True/False
    categoria_valida = d['categoria'] in ("medio", "alto")

    if es_multiplo and categoria_valida:
        print(d)



