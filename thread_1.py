#we can control the program according to us using thread..
'''import threading
import time
def Hello():
	print('wait for 5 sec')
	time.sleep(5)
	print('welcome to Hello')
t=threading.Thread(target=Hello)
t.start()

#passing any argument..
import threading
import time
def show(name):
	print('wait for 5 sec')
	time.sleep(5)
	print('welcome to hello',name)
t=threading.Thread(target=show,args=('Drashti',))
t.start()

#Enter a name for reverse after 1 second
import threading
import time

def show(reverse):
	x=name[::-1]
	for a in x:
		time.sleep(1)
		print(a)
name=input('enter name')
t=threading.Thread(target=show,args=(name,))
t.start()'''


#using threading in tkinter
import tkinter
from tkinter import *
import threading
import time
t=tkinter.Tk()
t.title('welcome')
t.geometry('1000x1000')

def inc():
	x=10
	while x<=30:
		i=0
		time.sleep(1)
		l.config(font=('Area',x))

def hi():
	t=threading.Thread(target=lt)
	t.start()
l=Label(t,text='PYTHON')
l.place(x=100,y=100)
b=Button(t,text='Size',command=hi)
b.place(x=100,y=150)
lt=['red','green','blue','orange']		
t.mainloop()

'''def inc():
	x=10
	while x<=20:
		x=x+1
		time.sleep(1)
		l.config(font=('Area',x))

def hi():
	t=threading.Thread(target=inc)
	t.start()
l=Label(t,text='PYTHON')
l.place(x=100,y=100)
b=Button(t,text='Size',command=hi)
b.place(x=100,y=150)
lt=['red','green','blue','orange']
lt.place(x=250,y=300)
t.mainloop()'''

