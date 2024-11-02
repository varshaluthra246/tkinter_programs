#CheckBox
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)

Checkbtn1 = IntVar()
Checkbtn2 = IntVar()

select = Checkbutton(win,text='Male')
select.pack()

select = Checkbutton(win,text='female')
select.pack()

win.mainloop()


