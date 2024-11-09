#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Text – многострочное текстовое поле.

from tkinter import *

if __name__ == "__main__":
    root = Tk()

    text = Text(width=25, height=5, bg="darkgreen",
                fg='white', wrap=WORD)

    text.pack()
    root.mainloop()
