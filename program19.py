#Top Level and Destroy
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

def func():
    top.destroy()
    win.destroy()

top = Toplevel()

btn = Button(top, text = "Close Window", command = func).pack()



win.mainloop()
