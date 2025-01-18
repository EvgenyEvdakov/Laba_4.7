#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Text и Scrollbar.

from tkinter import *


if __name__ == "__main__":
    root = Tk()

    text = Text(width=20, height=7)
    text.pack(side=LEFT)

    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)

    root.mainloop()
