#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод pack. Используем следующие два свойства – fill (заполнение) и expand (расширение).
# По-умолчанию expand равен нулю (другое значение – единица), а fill – NONE (другие значения BOTH , X , Y ).
# Создадим окно с одной меткой:

from tkinter import *

if __name__ == "__main__":
    root = Tk()
    l1 = Label(text="This is a label",
               width=30, height=10,
               bg="lightgreen")
    l1.pack(expand=1, fill=Y)
    root.mainloop()
