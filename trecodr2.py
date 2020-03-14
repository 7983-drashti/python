import tkinter
from tkinter import *
t=tkinter.Tk()
t.title("Database")
t.geometry('500x500')
l1=Label(t,text='Employee no')
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
b=Button(t,text='Delete',fg='black')
b.place(x=100,y=100)
t.mainloop()