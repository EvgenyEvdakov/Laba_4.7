#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Entry – однострочное текстовое поле.

from tkinter import *


def insert():
    e1.insert(0, "Tkinter - GUI ")


if __name__ == "__main__":
    root = Tk()
    e1 = Entry(width=50)
    but = Button(text="Вставить", command=insert)

    e1.pack()
    but.pack()
    root.mainloop()
