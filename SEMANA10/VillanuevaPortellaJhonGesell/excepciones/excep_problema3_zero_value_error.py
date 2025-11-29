try:
    a = float(input('Ingrese el primer número: '))
    b = float(input('Ingrese el segundo número: '))
    resultado = a / b
    print(f'La división es: {resultado}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - No se puede dividir por cero: {e}')
except ValueError as e:
    print(f'ValueError - Entrada no válida, debe ser numérica: {e}')
print('Continuamos...')
