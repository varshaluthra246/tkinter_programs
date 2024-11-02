#Creating a menu, menu-button, Option Menu, Separator
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

def demo():
    pass

my_menu = Menu(win)
win.config(menu = my_menu)

#file
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu = file_menu) 
file_menu.add_cascade(label = "New", command = demo)
file_menu.add_cascade(label = "Open", command = demo)

#edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu = edit_menu) 
edit_menu.add_cascade(label = "Undo", command = demo)
edit_menu.add_separator()
edit_menu.add_cascade(label = "Cut", command = demo)

win.mainloop()
