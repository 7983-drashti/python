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
	s="select rollno,bookid,actualReturnDate from return_book  where rollno=%d"%(e)
	try:
		cur=db.cursor()
		cur.execute(s)
		res=cur.fetchone()
		e2.insert(0,res[1])
		e3.insert(0,res[2])
	except Exception as es:
		print('any issue',es)
		db.close()
l1=Label(t,text='rollno',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
l2=Label(t,text='bookid',font=10)
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=250,y=100)
l3=Label(t,text='actual_return_date',font=10)
l3.place(x=100,y=150)
e3=Entry(t,bd=2,width=20)
e3.place(x=250,y=150)
l4=Label(t,text='return_book_find',font=10)
l4.place(x=150,y=20)
b=Button(t,text='Find',fg='black',bg='pink',font=10,command=search)
b.place(x=100,y=200)
b=Button(t,text='Exit',bg='pink',fg='black',font=10,command=ex)
b.place(x=200,y=200)
t.mainloop()