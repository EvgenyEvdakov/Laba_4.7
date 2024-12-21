#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Text. Методы get и delete могут принимать не два, а один аргумент.
# В таком случае будет обрабатываться только один символ в указанной позиции.

from tkinter import *


def insert_text():
    s = "Hello World"
    text.insert(1.0, s)


def get_text():
    s = text.get(1.0, END)
    label['text'] = s


def delete_text():
    text.delete(1.0, END)


if __name__ == "__main__":
    root = Tk()

    text = Text(width=25, height=5)
    text.pack()

    frame = Frame()
    frame.pack()

    Button(frame, text="Вставить", command=insert_text).pack(side=LEFT)
    Button(frame, text="Взять", command=get_text).pack(side=LEFT)
    Button(frame, text="Удалить", command=delete_text).pack(side=LEFT)

    label = Label()
    label.pack()

    root.mainloop()
