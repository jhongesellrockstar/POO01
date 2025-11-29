add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#Funcion map()
#map(funcion,iterable1, iterable2,....)

#Elevar al cuadrado cada numero de una lista
def elevar_cuadrado(n):
    return n*n

numeros=[1,2,3,4,5]
resultados=list(map(elevar_cuadrado,numeros))
print(resultados)

#Con una funcion Lambda
numeros=[1,2,3,4,5]
resultados_lambda=list(map(lambda x:x**2,numeros))
print(resultados_lambda)

#Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", squared_numbers )

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)