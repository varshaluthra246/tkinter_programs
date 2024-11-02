from tkinter import *
from tkinter import ttk
import tkinter as tk

#function coding:
exp = " "
def press(num):
    global exp
    exp+=str(num)     #exp = exp + str(num) 
    equation.set(exp)

def clear():
    global exp
    exp = " "
    equation.set(exp)
    
def action():
    global exp
    exp = " Next Line : "
    equation.set(exp)

#end function coding:

key = tk.Tk()
key.title("keyboard by varsha")
key.iconbitmap("apple.ico")
#set window size
#key.geometry('1010*250')
key.maxsize(width = 1010, height = 250)
key.minsize(width = 1010, height = 250)

#entry box
equation = tk.StringVar()
dis_entry = ttk.Entry(key, state = 'readonly', textvariable = equation)
dis_entry.grid(rowspan = 1, columnspan = 100, ipadx = 999, ipady = 20)

#background color
key.configure(bg = 'skyblue')

#button
#for first line
q = ttk.Button(key, text = "Q", width =6,command = lambda : press('Q'))
q.grid(row = 1, column = 0, ipadx = 6, ipady = 10)

w = ttk.Button(key, text = "W",width =6, command = lambda : press('W'))
w.grid(row = 1, column = 1, ipadx = 6, ipady = 10)

e = ttk.Button(key, text = "E",width =6, command = lambda : press('E'))
e.grid(row = 1, column = 2, ipadx = 6, ipady = 10)

r = ttk.Button(key, text = "R",width =6, command = lambda : press('R'))
r.grid(row = 1, column = 3, ipadx = 6, ipady = 10)

t = ttk.Button(key, text = "T", width =6,command = lambda : press('T'))
t.grid(row = 1, column = 4, ipadx = 6, ipady = 10)

y = ttk.Button(key, text = "Y", width =6,command = lambda : press('Y'))
y.grid(row = 1, column = 5, ipadx = 6, ipady = 10)

u = ttk.Button(key, text = "U", width =6,command = lambda : press('U'))
u.grid(row = 1, column = 6, ipadx = 6, ipady = 10)

i = ttk.Button(key, text = "I",width =6, command = lambda : press('I'))
i.grid(row = 1, column = 7, ipadx = 6, ipady = 10)

o = ttk.Button(key, text = "O",width =6, command = lambda : press('O'))
o.grid(row = 1, column = 8, ipadx = 6, ipady = 10)

p = ttk.Button(key, text = "P",width =6, command = lambda : press('P'))
p.grid(row = 1, column = 9, ipadx = 6, ipady = 10)

cur = ttk.Button(key, text = "{", width =6, command = lambda : press('{'))
cur.grid(row = 1, column = 10, ipadx = 6, ipady = 10)

cur_c = ttk.Button(key, text = "}", width =6, command = lambda : press('}'))
cur_c.grid(row = 1, column = 11, ipadx = 6, ipady = 10)

back_slash = ttk.Button(key, text = "\\", width =6, command = lambda : press('\\'))
back_slash.grid(row = 1, column = 12, ipadx = 6, ipady = 10)

#def clear():
#     pass

clear =ttk.Button(key, text = "clear", width = 6, command = clear)
clear.grid(row = 1, column = 13, ipadx = 6, ipady = 10)

#second line
a = ttk.Button(key, text = "A", width =6,command = lambda : press('A'))
a.grid(row = 2, column = 0, ipadx = 6, ipady = 10)

s = ttk.Button(key, text = "S",width =6, command = lambda : press('S'))
s.grid(row = 2, column = 1, ipadx = 6, ipady = 10)

d = ttk.Button(key, text = "D",width =6, command = lambda : press('D'))
d.grid(row = 2, column = 2, ipadx = 6, ipady = 10)

f = ttk.Button(key, text = "F",width =6, command = lambda : press('F'))
f.grid(row = 2, column = 3, ipadx = 6, ipady = 10)

g = ttk.Button(key, text = "G", width =6,command = lambda : press('G'))
g.grid(row = 2, column = 4, ipadx = 6, ipady = 10)

h = ttk.Button(key, text = "H", width =6,command = lambda : press('H'))
h.grid(row = 2, column = 5, ipadx = 6, ipady = 10)

j = ttk.Button(key, text = "J", width =6,command = lambda : press('J'))
j.grid(row = 2, column = 6, ipadx = 6, ipady = 10)

k = ttk.Button(key, text = "K",width =6, command = lambda : press('K'))
k.grid(row = 2, column = 7, ipadx = 6, ipady = 10)

l = ttk.Button(key, text = "L",width =6, command = lambda : press('L'))
l.grid(row = 2, column = 8, ipadx = 6, ipady = 10)

semi_co = ttk.Button(key, text = ";",width =6, command = lambda : press(';'))
semi_co.grid(row = 2, column = 9, ipadx = 6, ipady = 10)

d_colon = ttk.Button(key, text = '"',width =6, command = lambda : press('"'))
d_colon.grid(row = 2, column = 10, ipadx = 6, ipady = 10)

#def action():
#    pass
enter = ttk.Button(key, text = 'Enter',width =6, command = action)
enter.grid(row = 2, columnspan = 75, ipadx = 85, ipady = 10)

#third line
z = ttk.Button(key, text = "Z", width =6,command = lambda : press('Z'))
z.grid(row = 3, column = 0, ipadx = 6, ipady = 10)

x = ttk.Button(key, text = "X",width =6, command = lambda : press('X'))
x.grid(row = 3, column = 1, ipadx = 6, ipady = 10)

c = ttk.Button(key, text = "C",width =6, command = lambda : press('C'))
c.grid(row = 3, column = 2, ipadx = 6, ipady = 10)

v = ttk.Button(key, text = "V",width =6, command = lambda : press('V'))
v.grid(row = 3, column = 3, ipadx = 6, ipady = 10)

b = ttk.Button(key, text = "B", width =6,command = lambda : press('B'))
b.grid(row = 3, column = 4, ipadx = 6, ipady = 10)

n = ttk.Button(key, text = "N", width =6,command = lambda : press('N'))
n.grid(row = 3, column = 5, ipadx = 6, ipady = 10)

m = ttk.Button(key, text = "M", width =6,command = lambda : press('M'))
m.grid(row = 3, column = 6, ipadx = 6, ipady = 10)

lt = ttk.Button(key, text = "<",width =6, command = lambda : press('<'))
lt.grid(row = 3, column = 7, ipadx = 6, ipady = 10)

gt = ttk.Button(key, text = ">",width =6, command = lambda : press('>'))
gt.grid(row = 3, column = 8, ipadx = 6, ipady = 10)

slash = ttk.Button(key, text = "/",width =6, command = lambda : press('/'))
slash.grid(row = 3, column = 9, ipadx = 6, ipady = 10)

q_mark = ttk.Button(key, text = "?",width =6, command = lambda : press('?'))
q_mark.grid(row = 3, column = 10, ipadx = 6, ipady = 10)

coma = ttk.Button(key, text = ",",width =6, command = lambda : press(','))
coma.grid(row = 3, column = 11, ipadx = 6, ipady = 10)

dot = ttk.Button(key, text = ".",width =6, command = lambda : press('.'))
dot.grid(row = 3, column = 12, ipadx = 6, ipady = 10)

shift = ttk.Button(key, text = 'shift',width =6, command = lambda : press('shift'))
shift.grid(row = 3, column = 13, ipadx = 6, ipady = 10)

#fourth line

ctrl = ttk.Button(key, text= 'Ctrl', width = 6, command = lambda: press('Ctrl'))
ctrl.grid(row = 4, column = 0, ipadx = 6, ipady = 10)

fn = ttk.Button(key, text= 'fn', width = 6, command = lambda: press('fn'))
fn.grid(row = 4, column = 1, ipadx = 6, ipady = 10)

window = ttk.Button(key, text= 'Window', width = 6, command = lambda: press('window'))
window.grid(row = 4, column = 2, ipadx = 6, ipady = 10)

alt = ttk.Button(key, text= 'alt', width = 6, command = lambda: press('alt'))
alt.grid(row = 4, column = 3, ipadx = 6, ipady = 10)

space = ttk.Button(key, text= 'Space', width = 6, command = lambda: press(' '))
space.grid(row = 4, columnspan = 14, ipadx = 160, ipady = 10)

alt_gr = ttk.Button(key, text= 'Alt Gr', width = 6, command = lambda: press('alt_gr'))
alt_gr.grid(row = 4, column = 10, ipadx = 6, ipady = 10)

open_b = ttk.Button(key, text= '(', width = 6, command = lambda: press('('))
open_b.grid(row = 4, column = 11, ipadx = 6, ipady = 10)

close_b = ttk.Button(key, text= ')', width = 6, command = lambda: press(')'))
close_b.grid(row = 4, column = 12, ipadx = 6, ipady = 10)

def Tab():
    pass
tap = ttk.Button(key, text = 'Tab', width = 6, command = Tab)
tap.grid(row = 4, column = 13, ipadx = 20, ipady = 10)

                                                                             
key.mainloop()
