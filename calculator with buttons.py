import tkinter as tk
from tkinter import *


def bclick(number):
    current = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current) + str(number))


def bdelete():
    entry1.delete(0, END)


def ad():
    n = entry1.get()
    global number2
    global math
    math = "adition"
    number2 = int(n)
    entry1.delete(0, END)


def e():
    snumber = entry1.get()
    entry1.delete(0, END)
    if math == "adition":
        entry1.insert(0, int(number2) + int(snumber))
    if math == "subtraction":
        entry1.insert(0, int(number2) - int(snumber))
    if math == "dividing":
        entry1.insert(0, int(number2) / int(snumber))
    if math == "multiplication":
        entry1.insert(0, int(number2) * int(snumber))


def subtract():
    n = entry1.get()
    global number2
    global math
    math = "subtraction"
    number2 = int(n)
    entry1.delete(0, END)


def divide():
    n = entry1.get()
    global number2
    global math
    math = "dividing"
    number2 = int(n)
    entry1.delete(0, END)


def multiply():
    n = entry1.get()
    global number2
    global math
    math = "multiplication"
    number2 = int(n)
    entry1.delete(0, END)


root = Tk()
root.title("simple calculator")
entry1 = Entry(root, width=47, )
entry1.grid(row=0, column=0, sticky=W, columnspan=5, )
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: bclick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: bclick(2))
button3 = Button(root, text="3", padx=39.42, pady=20, command=lambda: bclick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: bclick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: bclick(5))
button6 = Button(root, text="6", padx=39.42, pady=20, command=lambda: bclick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: bclick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: bclick(8))
button9 = Button(root, text="9", padx=39.42, pady=20, command=lambda: bclick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: bclick(0))
adbutton = Button(root, text="+", padx=39, pady=20, command=ad)
cbutton = Button(root, text="clear", padx=30, pady=20, command=bdelete)
ebutton = Button(root, text="=", padx=134, pady=20, command=e)
subbutton = Button(root, text="-", padx=40, pady=20, command=subtract)
divbutton = Button(root, text="/", padx=41, pady=20, command=divide)
multbutton = Button(root, text="*", padx=40, pady=20, command=multiply)
button1.grid(row=2, column=0, sticky=W)
button2.grid(row=2, column=1, sticky=W)
button3.grid(row=2, column=2, sticky=W)
button4.grid(row=3, column=0, sticky=W)
button5.grid(row=3, column=1, sticky=W)
button6.grid(row=3, column=2, sticky=W)
button7.grid(row=4, column=0, sticky=W)
button8.grid(row=4, column=1, sticky=W)
button9.grid(row=4, column=2, sticky=W)
button0.grid(row=5, column=0, sticky=W)
adbutton.grid(row=5, column=1, sticky=W)
cbutton.grid(row=5, column=2, sticky=W)
subbutton.grid(row=6, column=0, sticky=W)
divbutton.grid(row=6, column=1, sticky=W)
multbutton.grid(row=6, column=2, sticky=W)
ebutton.grid(row=7, column=0, sticky=W, columnspan=5)
root.mainloop()
