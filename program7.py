#Button Example
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)

#label
lb1 = Label(win, text = "user name:")
lb1.place(x=10,y=10) 

#entry
var = StringVar()
ent = Entry(win, bg = "red", fg = "white", width = 10, bd = 5, textvariable = var)
ent.place(x=80,y=10)

#creating a button
btn = Button(win, text = "Submit", bg = "green")
btn.place(x=10, y=80)

win.mainloop()


