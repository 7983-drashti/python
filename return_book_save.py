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
	r=int(e1.get())
	bid=int(e2.get())
	actdate=(e3.get())

	s="insert into return_book values(%d,'%d','%s')"%(r,bid,actdate)
	try:
		cur.execute(s)
		db.commit()
		messagebox.showinfo('record saved')
		print('recodr saved')
	except Exception as es:
		messagebox.showinfo('any issue',es)
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

b=Button(t,text='Save',bg='pink',fg='black',font=10,command=savedata)
b.place(x=200,y=400)
l5=Label(t,text='return_book_Save',font=15,bg='Pink',fg='white')
l5.place(x=150,y=10)
b=Button(t,text='Exit',bg='pink',fg='black',font=10,command=ex)
b.place(x=300,y=400)

t.mainloop()
