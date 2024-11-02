#Button Example working
from tkinter import *
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)


#function create
def func():
    x = var.get()
    print(x)
    lb1.config(text=x, bg = "green")


#label
lb1 = Label(win, text = "user name:", bg = "Red", fg = "white")
lb1.place(x=10,y=10)


lb1 = Label(win, text = "No text entered ", bg = "Red", fg = "white" )
lb1.place(x=40,y=120) 

#entry
var = StringVar()
ent = Entry(win, bg = "red", fg = "white", width = 10, bd = 5, textvariable = var)
ent.place(x=80,y=10)

#creating a button
btn = Button(win, text = "Submit", bg = "green", command = func)
btn.place(x=10, y=80)

win.mainloop()


