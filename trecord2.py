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
	db=pymysql.connect('localhost','root','root','factory')
	cur=db.cursor()
	e=int(e1.get())
	s="delete from employee where empno=%d"%(e)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('data deleted')
		print('record deleted')
	except Exception as es:
		messagebox.showinfo('any issue',es)
		db.close()
l1=Label(t,text='Employee no',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
b=Button(t,text='Delete',fg='white',bg='grey',font=10,command=deldata)
b.place(x=100,y=100)
t.mainloop()