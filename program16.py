#lIST bOX
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("first tkinter program")
#win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

"""
lst = Listbox(win,width = 27)
lst.pack()
"""

"""
lst = Listbox(win,width = 27)
items = ['red','blue','purple','orange','pink','green']
for i in items:
    lst.insert(END,i)

lst.pack()
"""
def func():
    lst.delete(ANCHOR)

     
lst = Listbox(win,width = 27)
items = ['red','blue','purple','orange','pink','green']
for i in items:
    lst.insert(END,i)

btn = Button(win, text = "DELETE",command = func).pack()
lst.pack()

win.mainloop()
