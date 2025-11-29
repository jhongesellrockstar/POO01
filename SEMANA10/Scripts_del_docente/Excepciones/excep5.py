resultado=None
try:
    a=int(input('Primer Numero: '))
    b=int(input('Segundo Numero: '))
    if b==0:
        raise Exception('El denominador es igual a cero')
    resultado=a/b
except Exception as e:
    print(f'Exception - Ocurrio un error : {e}, {type(e)}')
else:
    print('Los valores ingresados son correctos')