#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок "Открыть" и
# "Сохранить". При клике на первую должен открываться на чтение файл, чье имя указано в поле класса Entry, а
# содержимое файла должно загружаться в поле типа Text.
# При клике на вторую кнопку текст, введенный пользователем в экземпляр Text, должен сохраняться в файле под именем,
# которое пользователь указал в однострочном текстовом поле.
# Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
# Для выполнения практической работы вам понадобится функция open языка Python и методы файловых
# объектов чтения и записи.

import tkinter as tk
from tkinter import messagebox
from typing import Optional


class FileManager:
    """Класс для работы с файлами: открытие, сохранение, чтение."""

    def open_file(self, filename: str) -> Optional[str]:
        """Открывает файл и возвращает его содержимое."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            messagebox.showerror("Ошибка", f"Файл {filename} не найден!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {str(e)}")
        return None

    def save_file(self, filename: str, content: str) -> None:
        """Сохраняет содержимое в файл."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            messagebox.showinfo("Успех", f"Файл {filename} успешно сохранен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")


class FileEditorApp:
    """Класс для интерфейса редактора файлов."""

    def __init__(self, root: tk.Tk, file_manager: FileManager) -> None:
        """Инициализация приложения."""
        self.root: tk.Tk = root
        self.file_manager: FileManager = file_manager
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создает графические элементы интерфейса."""
        # Создаем однострочное текстовое поле для ввода имени файла
        self.filename_entry: tk.Entry = tk.Entry(self.root, width=40, font=("Arial", 14))
        self.filename_entry.grid(row=0, column=0, padx=10, pady=10)

        # Создаем кнопки "Открыть" и "Сохранить"
        open_button: tk.Button = tk.Button(self.root, text="Открыть", width=15, font=("Arial", 14), command=self.open_file)
        open_button.grid(row=0, column=1, padx=10, pady=10)

        save_button: tk.Button = tk.Button(self.root, text="Сохранить", width=15, font=("Arial", 14), command=self.save_file)
        save_button.grid(row=0, column=2, padx=10, pady=10)

        # Создаем фрейм для текстового поля и полосы прокрутки
        frame: tk.Frame = tk.Frame(self.root)
        frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Создаем многострочное текстовое поле
        self.text_field: tk.Text = tk.Text(frame, width=60, height=15, font=("Arial", 14))
        self.text_field.grid(row=0, column=0, padx=5, pady=5)

        # Создаем полосу прокрутки для текстового поля
        scrollbar: tk.Scrollbar = tk.Scrollbar(frame, command=self.text_field.yview)
        scrollbar.grid(row=0, column=1, sticky="ns", pady=5)

        # Связываем полосу прокрутки с текстовым полем
        self.text_field.config(yscrollcommand=scrollbar.set)

    def open_file(self) -> None:
        """Открывает файл и загружает его содержимое в текстовое поле."""
        filename = self.filename_entry.get()
        content = self.file_manager.open_file(filename)
        if content is not None:
            self.text_field.delete(1.0, tk.END)
            self.text_field.insert(tk.END, content)

    def save_file(self) -> None:
        """Сохраняет содержимое текстового поля в файл."""
        filename = self.filename_entry.get()
        content = self.text_field.get(1.0, tk.END)
        self.file_manager.save_file(filename, content)


def main() -> None:
    """Основная функция, инициализирует и запускает приложение."""
    root: tk.Tk = tk.Tk()
    root.title("Редактор файлов")

    # Создаем экземпляр FileManager
    file_manager: FileManager = FileManager()

    # Создаем и запускаем приложение
    app: FileEditorApp = FileEditorApp(root, file_manager)
    root.mainloop()


if __name__ == "__main__":
    main()



