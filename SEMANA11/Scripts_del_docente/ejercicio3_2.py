#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()

#Titulo de la Ventana
root.title('Curso Tkinter')

#Entrada de datos
entrada=Entry(root)
entrada.insert(0,'Escriba su nombre')
entrada.bind('<Button-1>',lambda x: entrada.delete(0,END))
#entrada.bind('<Key>',lambda x: entrada.delete(0,END))
entrada.pack()

#Evento para el boton 2
def pulsar_boton():
    #print('boton pulsado')
    texto=entrada.get()
    #Label(root,text='Boton Pulsado').pack()
    Label(root,text=f'{texto}').pack()

#Boton 1
#Button(root,text='¡Pulsame!').pack()
Button(root,text='¡Pulsame!',command=pulsar_boton).pack()

#Bucle de ejecucion
root.mainloop()