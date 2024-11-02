#Radio working
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)

#def func():
#    print(var.get())
def func():
    if var.get() == 0:
        print("Male")
    else:
        print("female")
var = IntVar()

radio = Radiobutton(win, text = "Male", value = 0, variable=var).pack()
radio = Radiobutton(win, text = "Female", value = 1,variable=var).pack()

btn = Button(win, text = "submit", command = func).pack()

win.mainloop()
