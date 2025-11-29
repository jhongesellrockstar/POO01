datos = [10, 20, 30, 40, 50]

print(f'Lista: {datos}')
while True:
    try:
        idx = int(input('Ingrese un índice (0 a {0}): '.format(len(datos) - 1)))
        valor = datos[idx]
    except ValueError as e:
        print(f'ValueError - Debe ingresar un número entero: {e}')
        continue
    except IndexError as e:
        print(f'IndexError - Índice fuera de rango: {e}')
        continue
    else:
        print(f'Valor en datos[{idx}] = {valor}')
        break
print('Continuamos...')
