#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()

#Titulo de la Ventana
root.title('Curso de Tkinter')

#Tamaño de la ventana
#ancho=800, largo=600,posicion x=560, y=240
root.geometry('800x600+560+240')

#Creacion de etiquetas
Label(root,text='Mi primer Programa 😍').grid(row=0,column=10)
mensaje2=Label(root,text='Segunda etiqueta')
print('prueba')

#Mostrar etiquetas
mensaje2.grid(row=0,column=0)
#mensaje2.pack()
#mensaje.grid(row=1,column=0)
#mensaje2.grid(row=0,column=0)

#Bucle de ejecucion
root.mainloop()