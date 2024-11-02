#Photo-Image
from tkinter import *


win = Tk()
win.title("first tkinter program")
win.iconbitmap()
win.maxsize(width = 500, height = 300)
win.minsize(width = 500, height = 300)

file = PhotoImage(file = "tajmahal.jpg")
label = Label(win, image=file)
label.pack()

win.mainloop()
