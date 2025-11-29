from tkinter import *
root = Tk()
root.title('Problema')
root.geometry('800x600+560+240')
def pulsar_boton01():
    Label(root,text='Boton01 Pulsado').grid(row=0,column=1)
def pulsar_boton02():
    Label(root,text='Boton02 Pulsado').grid(row=1,column=1)
def pulsar_boton03():
    Label(root,text='Boton03 Pulsado').grid(row=2,column=1)
def pulsar_boton04():
    Label(root,text='Boton04 Pulsado').grid(row=3,column=1)
Button(root,text='Boton01',command=pulsar_boton01).grid(row=0,column=0)
Button(root,text='Boton02',command=pulsar_boton02).grid(row=1,column=0)
Button(root,text='Boton03',command=pulsar_boton03).grid(row=2,column=0)
Button(root,text='Boton04',command=pulsar_boton04).grid(row=3,column=0)
root.mainloop()