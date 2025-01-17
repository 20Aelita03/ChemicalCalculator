from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
from chempy import Substance

def click():
    var = Substance.from_formula(entry.get())
    label.config(text="Your formula: " + var.unicode_name + '\n' + 'Mass: ' + '%.3f' % var.mass)

root = Tk()

root.title("Chemical calculator")

frame = Frame(root, borderwidth=10, relief=GROOVE)
frame.pack()

entry = Entry(frame, width = 50)
entry.pack()


label = Label(frame)
label.pack()

button = Button(frame, text='Посчитать', command=click)
button.pack()

root.mainloop()
