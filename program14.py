#Frame
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

topheader = Frame(win)
topheader.pack()
#topheader.pack(side = RIGHT)
#topheader.pack(side = LEFT)

bottom = Frame(win)
bottom.pack(side = BOTTOM)

label = Label(topheader, text= "This is header portion")
label.pack()

label = Label(bottom, text= "This is bottom portion")
label.pack()

win.mainloop()
