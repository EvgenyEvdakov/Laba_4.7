#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: перепишите программу из пункта 8 так, чтобы интерфейс выглядел чуть другим образом, а именно,
# чтобы семь кнопок располагались горизонтально

import tkinter as tk
from typing import Callable, Dict


class ColorManager:
    """Класс для управления цветами."""

    def __init__(self, colors: Dict[str, str]) -> None:
        """Инициализация с набором цветов."""
        self.colors = colors

    def get_color_code(self, color_name: str) -> str:
        """Получить код цвета по его названию."""
        return self.colors.get(color_name, "#ffffff")  # По умолчанию белый цвет


class ColorApp:
    """Приложение для отображения и выбора цветов."""

    def __init__(self, root: tk.Tk, color_manager: ColorManager) -> None:
        """Инициализация приложения."""
        self.root: tk.Tk = root
        self.color_manager: ColorManager = color_manager
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создает графические элементы интерфейса."""
        # Метка для названия цвета
        self.label: tk.Label = tk.Label(self.root, text="желтый", width=20)
        self.label.pack(pady=5)

        # Поле для отображения кода цвета
        self.color_code_entry: tk.Entry = tk.Entry(self.root, width=10, justify="center")
        self.color_code_entry.insert(0, self.color_manager.get_color_code("желтый"))
        self.color_code_entry.pack(pady=5)

        # Создаем цветные квадраты в виде кнопок
        for color_name, color_code in self.color_manager.colors.items():
            btn: tk.Button = tk.Button(
                self.root, bg=color_code, width=4, height=2, command=self.create_update_color_command(color_name)
            )
            btn.pack(side=tk.LEFT, padx=2, pady=10)

    def create_update_color_command(self, selected_color: str) -> Callable[[], None]:
        """Возвращает функцию для обновления цвета."""

        def update_color() -> None:
            """Обновляет текстовое поле и метку с выбранным цветом."""
            color_code = self.color_manager.get_color_code(selected_color)
            self.color_code_entry.delete(0, tk.END)
            self.color_code_entry.insert(0, color_code)
            self.label.config(text=selected_color)

        return update_color


def main() -> None:
    """Основная функция, инициализирует и запускает приложение."""
    # Словарь с цветами
    colors: Dict[str, str] = {
        "красный": "#ff0000",
        "оранжевый": "#ff7f00",
        "желтый": "#ffff00",
        "зеленый": "#00ff00",
        "голубой": "#00ffff",
        "синий": "#0000ff",
        "фиолетовый": "#7f00ff",
    }

    root: tk.Tk = tk.Tk()
    root.title("Цветовая палитра")

    # Создаем экземпляр ColorManager
    color_manager: ColorManager = ColorManager(colors)

    # Создаем и запускаем приложение
    app: ColorApp = ColorApp(root, color_manager)
    root.mainloop()


if __name__ == "__main__":
    main()
