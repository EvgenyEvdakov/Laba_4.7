#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Button – кнопка

from tkinter import *

def change():
    b1['text'] = "Изменено"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'

if __name__ == "__main__":
    root = Tk()
    b1 = Button(
        text="Изменить",
        width=15,
        height=3
    )
    b1.config(command=change)
    b1.pack()
    root.mainloop()
