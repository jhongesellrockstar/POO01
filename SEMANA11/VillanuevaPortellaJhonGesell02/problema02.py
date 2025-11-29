from tkinter import *
root = Tk()
root.title('Problema')
root.geometry('800x600+600+300')
mensaje01=Label(root,text='Nombre:')
mensaje02=Label(root,text='Edad:')
mensaje01.grid(row=0,column=0)
mensaje02.grid(row=1,column=0)
entrada01=Entry(root)
entrada02=Entry(root)
entrada01.insert(0,'Escriba su nombre')
entrada02.insert(0,'Escriba su edad')
entrada01.bind('<Button-1>',lambda x: entrada01.delete(0,END))
entrada02.bind('<Button-1>',lambda x: entrada02.delete(0,END))
entrada01.grid(row=0,column=1)
entrada02.grid(row=1,column=1)

def pulsar_boton():
    texto01=entrada01.get()
    texto02=entrada02.get()
    Label(root,text=f'Mi nombre es {texto01}, tengo {texto02} anios').grid(row=3,column=1)
Button(root,text='Clic aquí',command=pulsar_boton).grid(row=2,column=1)


root.mainloop()