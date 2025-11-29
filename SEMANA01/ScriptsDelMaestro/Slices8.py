'''a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b)
print(id(a))
print(id(b))
c = a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)

#Ejemplo de Tupla
numbers=(1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])
numbers[0]=10'''

#Diccionario:
#Diccionario : Clave + valor

numbers={1:'uno',2:'dos',3:'tres'}
print(numbers)
print(numbers[2])
information={'Nombre':'carla',
            'Apellido':'Gomez',
             'Altura':1.65,
             'Edad':25}
print(information)
del information['Edad']
print(information)
print(type(information))
claves=information.keys()
print(claves)
valores=information.values()
print(valores)
pares=information.items()
print(pares)
contacts={'Carla':{'Apellido':'Gomez',
                   'Altura': 1.60,
                   'Edad': 29},
          'Diego':{'Apellido':'Antesana',
                   'Altura': 1.80,
                   'Edad': 32,}}
#print(contacts)
print(contacts['Carla'])


