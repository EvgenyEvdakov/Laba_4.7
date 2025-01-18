#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Checkbutton – флажок. С помощью методов select и deselect флажков можно их
# программно включать и выключать, это и необходимо проверить.

from tkinter import *


class CheckButton:
    def __init__(self, master, title):
        self.var = BooleanVar()
        self.var.set(0)
        self.title = title
        self.cb = Checkbutton(master, text=title, variable=self.var, onvalue=1, offvalue=0)
        self.cb.pack(side=LEFT)


def ch_on():
    for ch in checks:
        ch.cb.select()


def ch_off():
    for ch in checks:
        ch.cb.deselect()


if __name__ == "__main__":
    root = Tk()

    f1 = Frame()
    f1.pack(padx=10, pady=10)
    checks = []
    for i in range(10):
        checks.append(CheckButton(f1, i))

    f2 = Frame()
    f2.pack()

    button_on = Button(f2, text="Все ВКЛ", command=ch_on)
    button_on.pack(side=LEFT)

    button_off = Button(f2, text="Все ВЫКЛ", command=ch_off)
    button_off.pack(side=LEFT)

    root.mainloop()
