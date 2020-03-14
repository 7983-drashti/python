from tkinter.colorchooser import askcolor
from tkinter import messagebox
import sys
import tkinter
from tkinter import*
t=tkinter.Tk()
t.title("frame")
t.geometry('1000x1000')
def bk():
	r=askcolor(color='red',title='choose a color')
	l.config(bg=r[1])
def f():
	r=askcolor(color='green',title='choose a color')
	l.config(fg=r[1])
l=Label(t,text='DRASHTI',fg='black',font=15)
l.place(x=250,y=100)
b1=Button(t,text='Background',fg='black',command=bk)
b1.place(x=200,y=150)
b2=Button(t,text='Fontcolor',fg='black',command=f)
b2.place(x=300,y=150)

def ex():
	if(messagebox.askyesno('sure','Want to quit')):
		sys.exit()
	else:
		messagebox.showinfo('Thanks')
b3=Button(t,text='Exit',command=ex)
b3.place(x=200,y=200)
t.mainloop()


c=Canvas(t,height=800,width=800,bd=2,bg='green')
c.place(x=10,y=10)
c.create_line(30,50,300,500,fill='blue')#x1,y1,x2,y2
c.create_rectangle(200,300,101,202,fill='red')#height,width,x,y
c.create_oval(500,500,60,70,fill='pink')

p=[50,200,200,50,400,200]#x1,y1,x2,y2,x3,y3 coordinates...
c.create_polygon(p,fill='yellow')
img=PhotoImage(file='aa.gif')
c.create_image(100,200,image=img)

