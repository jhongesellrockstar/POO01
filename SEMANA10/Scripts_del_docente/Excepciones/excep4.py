while True:
    try:
        valor1=int(input('Ingrese primer valor: '))
        valor2=int(input('Ingrese segundo valor: '))
        suma=valor1+valor2
        print('La suma es: ', suma)
    except ValueError as e:
        print(f'Error - Debe ingresar numeros : {e}')
    else:
        print('Los valores ingresados fueron correctos')
        
    respuesta=input('Desea realizar la carga de otros valores?[s/n]')
    if respuesta=='n':
        break