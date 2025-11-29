try:
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    division = a / b
    print(f'La división es: {division}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - No se puede dividir por cero: {e}')
print('Continuamos...')
