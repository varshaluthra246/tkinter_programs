#Progress bar
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

progress = ttk.Progressbar(win)
progress.pack()

win.mainloop()
