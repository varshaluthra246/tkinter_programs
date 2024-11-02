#Canvas
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("first tkinter program")
#win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

canva = Canvas(win)
cord = 10, 50, 270, 210
#canva.create_arc(cord, start = 0, extent = 150, fill = "Red")
canva.create_arc(cord, start = 0, extent = 180, fill = "blue")
canva.create_line(cord)
canva.pack()

win.mainloop()
