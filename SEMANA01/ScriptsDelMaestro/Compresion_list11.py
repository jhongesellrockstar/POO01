#List comprehensions son una forma concisa y elegante de crear listas a partir de
#de otras secuencias o iterable como listas, rangos , etc'''

#List Comprehensions: [nueva_expresion for elemento in iterable if condicion]

'''nueva_expresion: Es la expresion que define como se modifica o procesa cada elemento del iterable y
                    cada uno de estos elementos va a generar la nueva lista.

   elemento: Variable que representa cada elemento del iterable original
   
   iterable: La secuencia o coleccion sobre la cual se itera.
   
   condicion: (opcional). Es una condicion para filtrar los elementos del iterable.
   
   '''
'''
#Imprimir numeros pares de la siguiente lista
numero=[1,2,3,4,5,6]
pares=[x for x in numero if x%2==0]
print(pares)
'''
'''
#Crear una lista de numeros de 0 al 9:
numeros=[x for x in range(10)]
print('Los numeros: ', numeros)
'''
'''
#Crear una lista de numeros cuadrados del 1 al 10
squares=[x**2 for x in range(1,11)]
print('Cuadrados: ',squares)
'''
'''
#tambien lo podemos hacer con el cubo(X3)

#transformar grados celcius a Farenheith
celsius=[0,10,20,30,40]
Farenheit=[(temp*9/5)+32 for temp in celsius]
print('Temperatura F: ', Farenheit)

'''
#Hallar los numeros pares del 1 al 20
num_par=[x for x in range(1,21) if x%2==0]
print(num_par)

'''
matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(len(matriz))
print(matriz[0][2])
for fila in matriz:
    #print(fila)
    for elemento in fila:
        print(elemento,end=' ')
print('-------------------')        
t=list(range(10))
print(t)

transposed1=[[row[i] for row in matriz] for i in range(len(matriz[0]))]
print(transposed1)

transposed=[]
for i in range(len(matriz[0])):
    transposed_row=[]
    for row in matriz:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)'''