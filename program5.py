#label example - grid(), pack() and place()
"""
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
lb1 = Label(win, text = "user name:")
lb1.pack() 
win.mainloop()
"""
"""
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
lb1 = Label(win, text = "user name:")
lb1.grid() 
win.mainloop()
"""
"""
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
lb1 = Label(win, text = "user name:")
lb1.place(x=10,y=100) 
win.mainloop()
"""
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
lb1 = Label(win, text = "user name:", bg = "Red", fg = "white", width = 10, height = 10)
lb1.place(x=10,y=100) 
win.mainloop()
