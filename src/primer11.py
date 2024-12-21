#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо изучить метод Теги.

from tkinter import *

if __name__ == "__main__":
    root = Tk()

    text = Text(width=50, height=10)
    text.pack()
    text.insert(1.0, "Hello world!\nline two")

    text.tag_add('title', 1.0, '1.end')
    text.tag_config('title', justify=CENTER,
                    font=("Verdana", 24, 'bold'))

    root.mainloop()
