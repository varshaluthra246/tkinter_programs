#Creating a menu-bar
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

my_menu = Menu(win)
win.config(menu = my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu) 

win.mainloop()
