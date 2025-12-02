#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()
#Titulo de la ventana
root.title('Curso de Tkinter')

#Entrada de Datos
entrada=Entry(root,
              background='springgreen',
              border=3,
              foreground='red',
              width=30
              ).pack()

#Funcion para el boton
def enviar():
    Label(root,
          text='Se ha pulsado el boton',
          background='skyblue',
          width=26
          ).pack()
    
#boton Enviar
boton=Button(root,
             text='Enviar',
             command=enviar,
             background='deepskyblue',
             foreground='gray98',
             border=3,
             width=25
             ).pack()

#Bucle de ejecucion
root.mainloop()