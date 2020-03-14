import tkinter 
from tkinter import *
import pymysql
from tkinter import messagebox
import sys
t=tkinter.Tk()
t.title('librarysystem')
t.geometry('1000x1000')

def ex():
	if (messagebox.askyesno('sure','want to exit')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')
def savedata():
	db=pymysql.connect('localhost','root','root','libsystem')
	cur=db.cursor()
	p=int(e1.get())
	q=(e2.get())
	r=(e3.get())
	sl=int(e4.get())
	t=int(e5.get())
	u=int(e6.get())
	s="insert into studentdata values(%d,'%s','%s','%d','%d',%d)"%(p,q,r,sl,t,u)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('record saved')
		print('recodr saved')
	except Exception as es:
		messagebox.showinfo('any issue',es)
	db.close()

l1=Label(t,text='bookid',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
l2=Label(t,text='bname',font=10)
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=250,y=100)
l3=Label(t,text='author',font=10)
l3.place(x=100,y=150)
e3=Entry(t,bd=2,width=20)
e3.place(x=250,y=150)
l4=Label(t,text='price',font=10)
l4.place(x=100,y=200)
e4=Entry(t,bd=2,width=20)
e4.place(x=250,y=200)
l5=Label(t,text='availstock',font=10)
l5.place(x=100,y=250)
e5=Entry(t,bd=2,width=20)
e5.place(x=250,y=250)
l6=Label(t,text='status',font=10)
l6.place(x=100,y=300)
e6=Entry(t,bd=2,width=20)
e6.place(x=250,y=300)

b=Button(t,text='Save',bg='pink',fg='black',font=10,command=savedata)
b.place(x=200,y=400)
l5=Label(t,text='Library System:book Record',font=15,bg='Pink',fg='black')
l5.place(x=150,y=10)
b=Button(t,text='Exit',bg='pink',fg='black',font=10,command=ex)
b.place(x=300,y=400)

t.mainloop()