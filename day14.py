'''import tkinter
from tkinter import*
import tkinter
t1=tkinter.Tk()
t1.title('event hnadling')
t1.geometry('1000x1000')
def ch1():     #functions...
	t1.config(bg='blue')
def ch2():
	t1.config(bg='green')
def ch3():
	t1.config(bg='pink')
bt=Button(t1,text='click',command=ch1)
bt.place(x=100,y=100)
bt1=Button(t1,text='click',command=ch2)
bt1.place(x=100,y=150)
bt2=Button(t1,text='click',command=ch3)
bt2.place(x=100,y=200)
t1.mainloop()'''

#home work..Screen 1
'''from tkinter import*# to add label ...
import tkinter
t2=tkinter.Tk()
t2.title('hw1')
t2.geometry('500x500')
l1=Label(t2,text='Apple',fg='black')
l1.place(x=100,y=100)

b1=Button(t2,text='+',fg='black')
b1.place(x=100,y=150)
b1=Button(t2,text='-',fg='black')
b1.place(x=150,y=150)
b1=Button(t2,text='red',fg='black')
b1.place(x=100,y=200)
b1=Button(t2,text='green',fg='black')
b1.place(x=150,y=200)
b1=Button(t2,text='exit',fg='black')
b1.place(x=120,y=250)
t2.mainloop()'''

#screen 2

import tkinter 
from tkinter import*
from tkinter import messagebox
t1=tkinter.Tk()
t1.title('Screen2')
t1.geometry('1000x1000')



l1=Label(t1,text='Customer Name',fg='black')
l1.place(x=100,y=100)
e1=Entry(t1,bd=2,width=40)
e1.place(x=250,y=100)

a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
c1=Checkbutton(t1,variable=a,onvalue=1,offvalue=0) 
c2=Checkbutton(t1,variable=b,onvalue=1,offvalue=0)
c3=Checkbutton(t1,variable=c,onvalue=1,offvalue=0)
c4=Checkbutton(t1,variable=d,onvalue=1,offvalue=0)
c1.place(x=100,y=200)
c2.place(x=100,y=250)
c3.place(x=100,y=300)
c4.place(x=100,y=350)

l2=Label(t1,text=' Name',fg='black')
l2.place(x=200,y=150)
nl1=Label(t1,text=' Item 1',fg='black')
nl1.place(x=200,y=200)
nl2=Label(t1,text=' Item 2',fg='black')
nl2.place(x=200,y=250)
nl3=Label(t1,text=' Item 3',fg='black')
nl3.place(x=200,y=300)
nl4=Label(t1,text=' Item 4',fg='black')
nl4.place(x=200,y=350)


l3=Label(t1,text='Price',fg='black')
l3.place(x=300,y=150)
pe1=Entry(t1,bd=2,width=5)
pe1.place(x=300,y=200)
pe2=Entry(t1,bd=2,width=5)
pe2.place(x=300,y=250)
pe3=Entry(t1,bd=2,width=5)
pe3.place(x=300,y=300)
pe4=Entry(t1,bd=2,width=5)
pe4.place(x=300,y=350)

l4=Label(t1,text='Quantity',fg='black')
l4.place(x=400,y=150)
e1=Entry(t1,bd=2,width=5)
e1.place(x=420,y=200)
e2=Entry(t1,bd=2,width=5)
e2.place(x=420,y=250)
e3=Entry(t1,bd=2,width=5)
e3.place(x=420,y=300)
e4=Entry(t1,bd=2,width=5)
e4.place(x=420,y=350)

b1=Button(t1,text='Total Price',fg='black')
b1.place(x=250,y=400)
t1.mainloop()

#Screen 3


'''import tkinter
from tkinter import*
t=tkinter.Tk()
t.title('Screen 3')
t.geometry('500x500')

l1=Label(t,text='Mango')
l1.place(x=100,y=100)

sp=Spinbox(t,from_=0,to=50)
sp.place(x=100,y=150)
t.mainloop()
'''

