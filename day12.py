#Tkinter
'''import tkinter
t=tkinter.Tk()
t.title("my first frame")
t.geometry('500x500')# methods should be use before main loop...
t.mainloop() #for tkinter screen..'''

from tkinter import ttk
from tkinter import*
import tkinter
t=tkinter.Tk()
t.title("my first frame")
t.geometry('500x500')
l=Label(t,text='Name please',bg='red',fg='yellow')# label place between geometry and mainloop..
l.place(x=100,y=50)
e=Entry(t,bd=2,width=20)
e.place(x=250,y=50)
l1=Label(t,text='Gender',bg='red',fg='yellow')
l1.place(x=100,y=100)
x=IntVar()
r1=Radiobutton(t,text='Male',variable=x,value=1)
r2=Radiobutton(t,text='female',variable=x,value=0)
r1.place(x=250,y=100)
r2.place(x=400,y=100)
a=IntVar()
b=IntVar()
c1=Checkbutton(t,text='reading',variable=a,onvalue=1,offvalue=0)# 
c2=Checkbutton(t,text='reading',variable=b,onvalue=1,offvalue=0)
c1.place(x=250,y=200)
c2.place(x=400,y=200)
lt=Listbox(t)# for list box...
lt.insert(1,'Agra')
lt.insert(2,'Delhi')
lt.insert(3,'Bihar')
lt.insert(4,'Mumbai')
lt.insert(5,'Lucknow')
lt.place(x=250,y=300)
s=Scale(t,from_=0,to=100)#scale..
s.place(x=50,y=350)
sp=Spinbox(t,from_=0,to=100)
sp.place(x=100,y=300)
ltx=['Red','Green','Blue','Yellow']
cb=ttk.Combobox(t,values=ltx)
cb.place(x=400,y=500)

t.mainloop() #for tkinter screen..

