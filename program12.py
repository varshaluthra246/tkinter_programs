#Radio Button
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)

var = IntVar()

radio = Radiobutton(win, text = "Male", value = 0).pack()
radio = Radiobutton(win, text = "Female", value = 1).pack()

win.mainloop()
