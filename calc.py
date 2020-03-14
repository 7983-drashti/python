from tkinter import ttk
from tkinter import*
import tkinter
from tkinter import messagebox
t1=tkinter.Tk()
t1.title('Calculator')
t1.geometry('500x500')
def sum():
	a=int(e1.get())
	b=int(e2.get())
	c=a+b
	messagebox.showinfo('sum is',c)

def sub():
	a=int(e1.get())
	b=int(e2.get())
	c=a-b
	messagebox.showinfo('subtract is',c)
def mult():
	a=int(e1.get())
	b=int(e2.get())
	c=a*b
	messagebox.showinfo('multply is',c)
def divide():
	a=int(e1.get())
	b=int(e2.get())
	c=a/b
	messagebox.showinfo('divide is',c)
l1=Label(t1,text='enter first no.',fg='black')
l1.place(x=50,y=50)
e1=Entry(t1,bd=2,width=30)
e1.place(x=150,y=50)
l2=Label(t1,text='enter second no.',fg='black')
l2.place(x=50,y=100)
e2=Entry(t1,bd=2,width=30)
e2.place(x=150,y=100)
b1=Button(t1,text='+',fg='black',command=sum)
b1.place(x=150,y=150)
b2=Button(t1,text='-',fg='black',command=sub)
b2.place(x=200,y=150)
b3=Button(t1,text='*',fg='black',command=mult)
b3.place(x=250,y=150)
b4=Button(t1,text='/',fg='black',command=divide)
b4.place(x=300,y=150)
def ch():
	a=x.get()
	if a==1:
		t1.config(bg='red')
	if a==2:
		t1.config(bg='green')
	if a==3:
		t1.config(bg='blue')
	
x=IntVar()
r1=Radiobutton(t1,text='red',variable=x,value=1,command=ch)
r2=Radiobutton(t1,text='green',variable=x,value=2,command=ch)
r3=Radiobutton(t1,text='blue',variable=x,value=3,command=ch)
r1.place(x=200,y=300)
r2.place(x=200,y=350)
r3.place(x=200,y=400)
t1.mainloop()