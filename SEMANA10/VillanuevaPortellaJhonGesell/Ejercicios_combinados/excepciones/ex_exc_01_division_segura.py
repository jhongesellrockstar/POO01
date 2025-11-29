def division_segura(a, b):
    resultado = None
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError - No se puede dividir por cero: {e}')
    except TypeError as e:
        print(f'TypeError - Tipos no compatibles: {e}')
    except Exception as e:
        print(f'Exception - Ocurrió un error: {e}')
    return resultado


try:
    x = float(input('Ingrese el dividendo: '))
    y = float(input('Ingrese el divisor: '))
    r = division_segura(x, y)
    print(f'Resultado: {r}')
except Exception as e:
    print(f'Error de entrada: {e}')
print('Continuamos...')
