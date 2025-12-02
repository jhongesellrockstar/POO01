from tkinter import *
import os
root=Tk()
root.title('Tablero de ajedrez')
root.geometry("300x300")
"""marco1=LabelFrame(root,
                 padx=25,
                 pady=10,
                 foreground='red',
                 background='sea green',
                 )
marco1.grid(padx=1,pady=15,row=0,column=0,)

marco2=LabelFrame(root,
                 padx=25,
                 pady=10,
                 foreground='red',
                 background='palegreen',
                 )
marco2.grid(row=1,column=0,padx=5,pady=15)"""

boton01=Button(background='indian red',
             border=3,
             width=3
             )
boton01.grid(row=0,column=0,padx=25,pady=10)
boton02=Button(background='cyan',
             border=3,
             width=3
             )
boton02.grid(row=0,column=1,padx=10,pady=10)
boton03=Button(background='indian red',
             border=3,
             width=3
             )
boton03.grid(row=0,column=2,padx=25,pady=10)
boton04=Button(background='cyan',
             border=3,
             width=3
             )
boton04.grid(row=1,column=0,padx=25,pady=10)
boton05=Button(background='indian red',
             border=3,
             width=3
             )
boton05.grid(row=1,column=1,padx=25,pady=10)
boton06=Button(background='cyan',
             border=3,
             width=3
             )
boton06.grid(row=1,column=2,padx=25,pady=10)
boton07=Button(background='indian red',
             border=3,
             width=3
             )
boton07.grid(row=2,column=0,padx=25,pady=10)
boton08=Button(background='cyan',
             border=3,
             width=3
             )
boton08.grid(row=2,column=1,padx=25,pady=10)
boton09=Button(background='indian red',
             border=3,
             width=3
             )
boton09.grid(row=2,column=2,padx=25,pady=10)

root.mainloop()