import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import sys
t=tkinter.Tk()
t.title("Database")
t.geometry('1000x1000')

def ex():
	if(messagebox.askyesno('sure','want to quit')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')

def deldata():
	db=pymysql.connect('localhost','root','root','libsystem')
	cur=db.cursor()
	e=int(e1.get())
	s="delete from course where courseid='%s'"%(e)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('data deleted')
		print('record deleted')
	except Exception as es:
		messagebox.showinfo('any issue',es)
		db.close()

l1=Label(t,text='course id',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
l2=Label(t,text='cname',font=10)
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=250,y=100)
l3=Label(t,text='cduration',font=10)
l3.place(x=100,y=150)
e3=Entry(t,bd=2,width=20)
e3.place(x=250,y=150)

b=Button(t,text='Delete',fg='white',bg='grey',font=10,command=deldata)
b.place(x=100,y=400)
t.mainloop()