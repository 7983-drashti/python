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
	db=pymysql.connect('localhost','root','root','factory')
	e=int(e1.get())
	s="select * from  employee where empno=%d"%(e)
	try:
		cur.execute(s)
		res=cur.fetchall()
		for r in res:
			print('empno',r[0])
			print('name',r[1])
			print('city',r[2])
			print('salary',r[3])
		messagebox.showinfo('found')

	except Exception as es:
		messagebox.showinfo('any issue',es)
		db.close()
l1=Label(t,text='Employee no',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
b=Button(t,text='Find',fg='black',bg='pink',font=10,command=search)
b.place(x=100,y=100)
t.mainloop()