#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги.
# При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
# Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый, #ffff00 – желтый,
# #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.

import tkinter as tk
from typing import Dict


class ColorManager:
    """Класс для управления цветами."""

    def __init__(self, colors: Dict[str, str]) -> None:
        """Инициализация с набором цветов."""
        self.colors = colors

    def get_color_code(self, color_name: str) -> str:
        """Получает код цвета по его названию."""
        return self.colors.get(color_name, "Неизвестный цвет")


class ColorApp:
    """Приложение для отображения цветов радуги."""

    def __init__(self, root: tk.Tk, color_manager: ColorManager) -> None:
        """Инициализация приложения."""
        self.root: tk.Tk = root
        self.color_manager: ColorManager = color_manager
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создает графические элементы интерфейса."""
        # Метка для отображения кода цвета
        self.color_label: tk.Label = tk.Label(self.root, text="", font=("Arial", 14))
        self.color_label.grid(row=0, column=0, padx=5, pady=5)

        # Текстовое поле для отображения названия цвета
        self.color_entry: tk.Entry = tk.Entry(self.root, width=20, font=("Arial", 14))
        self.color_entry.grid(row=1, column=0, padx=5, pady=5)

        # Кнопки для каждого цвета
        for idx, (color_name, color_code) in enumerate(self.color_manager.colors.items()):
            button: tk.Button = tk.Button(
                self.root,
                text=color_name,   # Название цвета на кнопке
                bg=color_code,     # Цвет фона кнопки
                width=20,
                command=lambda code=color_code, name=color_name: self.set_color(code, name)
            )
            button.grid(row=2+idx, column=0, padx=5, pady=5)

    def set_color(self, color_code: str, color_name: str) -> None:
        """Устанавливает код цвета в текстовое поле и название цвета в метку."""
        self.color_entry.delete(0, tk.END)      # Очищаем текстовое поле
        self.color_entry.insert(0, color_name)  # Вставляем название цвета в текстовое поле
        self.color_label.config(text=color_code) # Обновляем метку, чтобы в ней был код цвета


def main() -> None:
    """Основная функция, инициализирует и запускает приложение."""
    # Словарь с цветами радуги и их кодами
    colors: Dict[str, str] = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff7d00",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#007dff",
        "Синий": "#0000ff",
        "Фиолетовый": "#7d00ff"
    }

    root: tk.Tk = tk.Tk()
    root.title("Цвета радуги")

    # Создаем экземпляр ColorManager
    color_manager: ColorManager = ColorManager(colors)

    # Создаем и запускаем приложение
    app: ColorApp = ColorApp(root, color_manager)
    root.mainloop()


if __name__ == "__main__":
    main()


