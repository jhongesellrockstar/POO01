#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()
#Titulo de la ventana
root.title('Curso de Tkinter')

'''Variables de control: IntVar, DoubleVar, StringVar, BooleanVar'''

opcion=IntVar()
opcion.set(1)

#Funcion para el boton de envio
def actualiza_radio(valor):
    Label(root,text=valor).pack()

#RadioButton
Radiobutton(root,
            text='Rojo',
            variable=opcion,
            value=1
            ).pack()

Radiobutton(root,
            text='Azul',
            variable=opcion,
            value=2
            ).pack()

Radiobutton(root,
            text='Verde',
            variable=opcion,
            value=3
            ).pack()

Radiobutton(root,
            text='Amarillo',
            variable=opcion,
            value=4
            ).pack()

#Boton de envio
boton_envia=Button(root,
                   text='Enviar',
                   command=lambda:actualiza_radio(opcion.get())).pack()

#Bucle de ejecucion
root.mainloop()