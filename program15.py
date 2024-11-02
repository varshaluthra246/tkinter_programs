#Message box or alert box
from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("first tkinter program")
#win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

def func():
    if var.get() == "":
        messagebox.showwarning("Warning", "Empty Field")
    else:
        #messagebox.showinfo("Success",var.get())
        messagebox.askyesno('Title','Do you want to exit?')
        win.destroy()
    
var = StringVar()
ent = Entry(win,textvariable = var)
ent.pack()

btn = Button(win, text = "click here", command=func)
btn.pack()

win.mainloop()

win.mainloop()
