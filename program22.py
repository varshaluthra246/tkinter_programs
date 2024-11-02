#Progress bar
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
#win.maxsize(width = 600, height = 300)
win.minsize(width = 600, height = 300)

progress = ttk.Progressbar(win, orient = HORIZONTAL, length = 100, mode = "determinate")

def bar():
    import time
    #progress['value'] = 100
    progress['value'] = 20
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    progress.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 20
    progress.update_idletasks()
    time.sleep(0.5)

    
    progress['value'] = 0
    

progress.pack(pady = 10)

btn = Button(win, text = "Start", command = bar).pack()

win.mainloop()
