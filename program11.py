#CheckBox Working
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)

def func():
    print(Checkbtn1.get())
    print(Checkbtn2.get())
    
Checkbtn1 = IntVar()
Checkbtn2 = IntVar()

select = Checkbutton(win,text='Male', variable = Checkbtn1, onvalue =1, offvalue= 0 )
select.pack()

select = Checkbutton(win,text='female', variable = Checkbtn2,onvalue =1, offvalue= 0)
select.pack()

btn = Button(win, text= "Data Get", command = func).pack()

win.mainloop()
