#ComboBox
from tkinter import *
from tkinter import ttk
win = Tk()
win.title("first tkinter program")
win.iconbitmap('apple.ico')
win.maxsize(width = 600, height = 300)
var = StringVar()
com = ttk.Combobox(win, width = 27)
#com['state'] = 'readonly'
com['values'] = ('January','Feb','March','April','May','June','july','August','September','October','november','December')
#com.current(0)

com.place(x=10, y=10)
win.mainloop()
