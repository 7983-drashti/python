from tkinter import *
import tkinter
t=tkinter.Tk()
t.title("my second frame")
t.geometry('500x500')
mb=Menu(t)
fm=Menu(mb)
fm.add_command(label='New')
fm.add_separator()
fm.add_command(label='Open')
fm.add_separator()
fm.add_command(label='Save')
fm.add_separator()
mb.add_cascade(label='File',menu=fm)
fm1=Menu(mb)
fm1.add_command(label='font')
fm1.add_separator()
fm1.add_command(label='format')
fm1.add_separator()
fm1.add_command(label='Style')
mb.add_cascade(label='edit')
t.config(menu=mb)
t.mainloop()