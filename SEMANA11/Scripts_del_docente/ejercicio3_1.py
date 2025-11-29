#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()

#Titulo de la Ventana
root.title('Curso Tkinter')

root.geometry('800x600+560+240')


#Evento para el boton 2
def pulsar_boton():
    print('boton pulsado')
    
    Label(root,text='Boton Pulsado').pack()
    
#Boton 1
#Button(root,text='¡Pulsame!').pack()
Button(root,text='¡Pulsame!',command=pulsar_boton).pack()

#Bucle de ejecucion
root,mainloop()