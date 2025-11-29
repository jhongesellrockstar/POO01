def leer_entero(mensaje='Ingrese un número entero: '):
    while True:
        try:
            valor = int(input(mensaje))
            print('Entrada válida.')
            return valor
        except ValueError as e:
            print(f'Error - Debe ingresar un entero válido: {e}')


n = leer_entero()
print(f'Entero leído: {n}')
print('Continuamos...')
