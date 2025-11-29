def divide(a, b):
    if isinstance(b, str) and len(b.strip()) == 1 and not b.strip().isdigit():
        raise ValueError('El divisor no puede ser un carácter.')
    if isinstance(a, str):
        a = float(a)
    if isinstance(b, str):
        b = float(b)
    return a / b


try:
    a_in = input('Ingrese el dividendo: ')
    b_in = input('Ingrese el divisor: ')
    resultado = divide(a_in, b_in)
    print(f'Resultado: {resultado}')
except ValueError as e:
    print(f'ValueError - Entrada inválida: {e}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - No se puede dividir por cero: {e}')
except TypeError as e:
    print(f'TypeError - Tipos no compatibles: {e}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}')
else:
    print('No se arrojó ninguna excepción.')
finally:
    print('Ejecución del bloque finally')
print('Continuamos...')
