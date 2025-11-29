from tkinter import *
root = Tk()
root.title('Curso de Tkinter')
root.geometry('600x450+50+75')
Label(root,text='grupo01, label01').grid(row=0,column=0)
Label(root,text='grupo02, label02').grid(row=1,column=1)
Label(root,text='grupo03, label03').grid(row=99,column=99)
Label(root,text='grupo04, label04').grid(row=100,column=100)
Label(root,text='grupo05, label05').grid(row=101,column=101)
Label(root,text='-'*20).grid(row=102,column=0)

mensaje1 = Label(root,text='GRUPO02, LABEL01')
mensaje1.grid(row=0,column=101)
root.mainloop()