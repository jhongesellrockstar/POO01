#Importaciones
from tkinter import *

#Creacion de la ventana principal
root=Tk()
#Titulo de la ventana
root.title('Curso de Tkinter')

#Marco
marco1=LabelFrame(root,
                 text='Marco de la ventana principal',
                 padx=20,
                 pady=20
                 )
marco1.grid(padx=15,pady=15,row=0,column=0,)

marco2=LabelFrame(root,
                 text='Enviar',
                 padx=20,
                 pady=20
                 )
marco2.grid(row=1,column=0,padx=5,pady=15)

marco3=LabelFrame(root,
                 text='Resultado',
                 padx=20,
                 pady=20
                 )
marco3.grid(row=0,column=1,padx=5,pady=15)

#Entrada de Datos
entrada=Entry(marco1,
              background='springgreen',
              border=3,
              foreground='red',
              width=30
              )
entrada.pack()
entrada.insert(0,'Escriba su nombre...')
entrada.bind('<Button-1>',lambda e: entrada.delete(0,END))

#Funcion para el boton
def enviar():
    nombre=entrada.get()
    Label(marco3,
          text=f'Hola {nombre}',
          background='skyblue',
          width=27
          ).pack()
    
#boton Enviar
boton=Button(marco2,
             text='Enviar',
             command=enviar,
             background='deepskyblue',
             foreground='gray98',
             border=3,
             width=25
             ).pack()


#Bucle de ejecucion
root.mainloop()