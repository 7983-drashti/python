#savr employee details...Screen..
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import sys
t=tkinter.Tk()
t.title("Database")
t.geometry('1000x1000')
def ex():
	if(messagebox.askyesno('sure','Want to quit')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')

def savedata():
	db=pymysql.connect('localhost','root','root','factory')
	cur=db.cursor()
	e=int(e1.get())
	n=(e2.get())
	c=(e3.get())
	sl=int(e4.get())
	s="insert into employee values(%d,'%s','%s',%d)"%(e,n,c,sl)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('record saved')
		print('recodr saved')
	except Exception as es:
		messagebox.showinfo('any issue',es)
	db.close()

l1=Label(t,text='Employee no',font=10)
l1.place(x=100,y=50)
e1=Entry(t,bd=2,width=20)
e1.place(x=250,y=50)
l2=Label(t,text='Enter emp name',font=10)
l2.place(x=100,y=100)
e2=Entry(t,bd=2,width=20)
e2.place(x=250,y=100)
l3=Label(t,text='Enter city',font=10)
l3.place(x=100,y=150)
e3=Entry(t,bd=2,width=20)
e3.place(x=250,y=150)
l4=Label(t,text='Enter Salary',font=10)
l4.place(x=100,y=200)
e4=Entry(t,bd=2,width=20)
e4.place(x=250,y=200)
b=Button(t,text='Save',bg='green',fg='white',font=10,command=savedata)
b.place(x=200,y=250)
l5=Label(t,text='Employee Details',font=15,bg='green',fg='white')
l5.place(x=150,y=10)
b=Button(t,text='Exit',bg='green',fg='white',font=10,command=ex)
b.place(x=300,y=250)
t.mainloop()