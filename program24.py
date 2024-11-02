#Scroll Bar using text area
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

scroll = Scrollbar(win)
scroll.pack(side = RIGHT, fill = Y)
mylist = Text(win, yscrollcommand = Y)
for i in range(1000):
    mylist.insert(END,i)
mylist.pack(side = LEFT, fill = Y)
scroll.config(command = mylist.yview)
    



win.mainloop()
