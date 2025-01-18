#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить способ вставки виджетов в текстовое поле.

from tkinter import *


def smile():
    label = Label(text=":)", bg="yellow")
    text.window_create(INSERT, window=label)


if __name__ == "__main__":
    root = Tk()

    text = Text(width=50, height=10)
    text.pack()

    button = Button(text=":)", command=smile)
    button.pack()

    root.mainloop()
