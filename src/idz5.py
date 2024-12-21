#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: виджеты Radiobatton и Checkbutton поддерживают большинство свойств
# оформления внешнего вида, которые есть у других элементов графического интерфейса.
# При этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен
# единице, в этом случае радиокнопка выглядит как нормальная радиокнопка. Однако если
# присвоить этой опции ноль, то виджет Radiobutton становится похожим на обычную кнопку
# по внешнему виду. Но не по смыслу.
# Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
# индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь кнопка включается, то в
# метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
# не должно.

import tkinter as tk


class ContactApp:
    """Приложение для отображения информации о контактах."""

    def __init__(self, root, contacts):
        self.contacts = contacts
        self.selected_contact = tk.StringVar(value="")

        # Создание интерфейса
        self.create_widgets(root)

    def create_widgets(self, root):
        """Создает интерфейс приложения."""
        # Фрейм для радиокнопок
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Создание радиокнопок
        for name in self.contacts.keys():
            rb = tk.Radiobutton(
                frame,
                text=name,
                variable=self.selected_contact,
                value=name,
                indicatoron=0,
                width=10,
                command=lambda n=name: self.show_info(n)
            )
            rb.pack(pady=5)

        # Метка для отображения информации
        self.info_label = tk.Label(root, text="", width=30, anchor="w", font=("Arial", 14))
        self.info_label.pack(side=tk.LEFT, padx=10, pady=10)

    def show_info(self, name):
        """Обновляет метку информацией, связанной с кнопкой."""
        info = self.contacts.get(name, "")
        self.info_label.config(text=info)


if __name__ == "__main__":
    contacts = {
        "Имя": "Евгений",
        "Фамилия": "Евдаков",
        "Отчество": "Владимирович"
    }

    # Создание главного окна
    root = tk.Tk()
    root.title("Студент")

    # Запуск приложения
    app = ContactApp(root, contacts)

    # Запуск главного цикла обработки событий
    root.mainloop()
