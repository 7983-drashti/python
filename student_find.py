import tkinter
from tkinter import *
import sys
from tkinter import messagebox
import pymysql
t=tkinter.Tk()
t.title("Database")
t.geometry('1000x1000')
def ex():
	if (messagebox.askyesno('want to exit','sure')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')

def search():
	db=pymysql.connect('localhost','root','root','libsystem')
	e=int(e1.get())
	s="select name,address,city,email,courseid,status from  studentdata  where rollno=%d"%(e)
	try:
		cur=db.cursor()
		cur.execute(s)
		res=cur.fetchone()
		e2.insert(0,res[0])
		e3.insert(0,res[1])
		e4.insert(0,res[2])
		e5.insert(0,res[3])
		e6.insert(0,res[4])
		e7.insert(0,res[5])
	except Exception as es:
		print('any issue',es)
		db.close()
l1=Label(t,text='rollno',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
l2=Label(t,text='name',font=10)
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=250,y=100)
l3=Label(t,text='address',font=10)
l3.place(x=100,y=150)
e3=Entry(t,bd=2,width=20)
e3.place(x=250,y=150)
l4=Label(t,text='city',font=10)
l4.place(x=100,y=200)
e4=Entry(t,bd=2,width=20)
e4.place(x=250,y=200)
l5=Label(t,text='email',font=10)
l5.place(x=100,y=250)
e5=Entry(t,bd=2,width=20)
e5.place(x=250,y=250)
l6=Label(t,text='courseid',font=10)
l6.place(x=100,y=300)
e6=Entry(t,bd=2,width=20)
e6.place(x=250,y=300)
l7=Label(t,text='status',font=10)
l7.place(x=100,y=350)
e7=Entry(t,bd=2,width=20)
e7.place(x=250,y=350)
b=Button(t,text='Find',fg='black',bg='pink',font=10,command=search)
b.place(x=100,y=400)
t.mainloop()