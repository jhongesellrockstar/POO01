meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

try:
    numero = int(input('Ingrese el número del mes (1-12): '))
    print(f'El mes es: {meses[numero - 1]}')
except IndexError as e:
    print(f'IndexError - Número de mes fuera de rango: {e}')
except ValueError as e:
    print(f'ValueError - Debe ingresar un número entero: {e}')
print('Continuamos...')
