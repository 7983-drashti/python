import tkinter
from tkinter import *
t=tkinter.Tk()
t.title("Database")
t.geometry('1000x1000')
l1=Label(t,text='Employee no',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
b=Button(t,text='Find',fg='black',bg='pink',font=10)
b.place(x=100,y=100)
t.mainloop()