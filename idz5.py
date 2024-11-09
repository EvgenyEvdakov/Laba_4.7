#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# напишите программу, в которой имеется несколько объединенных в группу радиокнопок, индикатор которых выключен
# ( indicatoron=0 ). Если какая-нибудь кнопка включается, то в метке должна отображаться соответствующая ей информация.
# Обычных кнопок в окне быть не должно.

import tkinter as tk
from tkinter import StringVar
from typing import List


class PersonSelectionApp:
    """Класс приложения для выбора данных о человеке и обновления информации."""

    def __init__(self, root: tk.Tk) -> None:
        """Инициализация приложения."""
        self.root = root
        self.selected_person = StringVar(value="")

        # Настроим виджеты
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создает интерфейс с кнопками и меткой для отображения информации."""
        # Фрейм для вертикального размещения кнопок
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Создаем радиокнопки
        people: List[str] = ["Фамилия", "Имя", "Отчество"]
        for person in people:
            rb = tk.Radiobutton(buttons_frame, text=person, variable=self.selected_person, value=person,
                                indicatoron=0, width=10, command=self.update_label, relief="solid")
            rb.pack(fill="x", pady=2)

        # Метка для отображения выбранной информации
        self.label = tk.Label(self.root, text=" ", width=20, anchor="w", font=("Arial", 12))
        self.label.pack(side=tk.LEFT, padx=10, pady=10)

    def update_label(self) -> None:
        """Обновляет текст метки в зависимости от выбранной кнопки."""
        selection = self.selected_person.get()
        if selection == "Фамилия":
            self.label.config(text="Евдаков")
        elif selection == "Имя":
            self.label.config(text="Евгений")
        elif selection == "Отчество":
            self.label.config(text="Владимирович")


def main() -> None:
    """Основная функция, создающая и запускающая приложение."""
    root = tk.Tk()
    root.title("Выбор человека")

    app = PersonSelectionApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()



