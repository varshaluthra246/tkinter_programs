#entry box or Text Field
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
lb1 = Label(win, text = "user name:")
lb1.place(x=10,y=10) 

ent = Entry(win, bg = "red", fg = "white", width = 10, bd = 5)
ent.place(x=80,y=10)
win.mainloop()
