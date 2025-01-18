#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
# должен отображаться в метке. Если арифметическое действие выполнить невозможно
# (например, если были введены буквы, а не числа), то в метке должно появляться слово
# "ошибка".

import tkinter as tk
from typing import Union


class Calculator:
    """Класс калькулятора, выполняющий арифметические операции."""

    def calculate(self, num1: float, num2: float, operation: str) -> Union[float, str]:
        """Выполняет арифметическую операцию и возвращает результат."""
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2 if num2 != 0 else "ошибка"
        return "ошибка"


class CalculatorApp:
    """Приложение калькулятора с графическим интерфейсом."""

    def __init__(self, root: tk.Tk, calculator: Calculator) -> None:
        """Инициализация интерфейса и калькулятора."""
        self.root = root
        self.calculator = calculator
        self.create_widgets()

    def create_widgets(self) -> None:
        """Создает графические элементы интерфейса."""
        # Поля ввода для двух чисел
        self.entry1 = tk.Entry(self.root, width=10)
        self.entry1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.entry2 = tk.Entry(self.root, width=10)
        self.entry2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Кнопки операций
        btn_add = tk.Button(self.root, text="+", width=5, command=lambda: self.calculate("+"))
        btn_add.grid(row=2, column=0, columnspan=2, padx=5, pady=2)

        btn_sub = tk.Button(self.root, text="-", width=5, command=lambda: self.calculate("-"))
        btn_sub.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        btn_mul = tk.Button(self.root, text="*", width=5, command=lambda: self.calculate("*"))
        btn_mul.grid(row=4, column=0, columnspan=2, padx=5, pady=2)

        btn_div = tk.Button(self.root, text="/", width=5, command=lambda: self.calculate("/"))
        btn_div.grid(row=5, column=0, columnspan=2, padx=5, pady=2)

        # Метка для отображения результата
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate(self, operation: str) -> None:
        """Получает значения из полей ввода и вызывает калькулятор для выполнения операции."""
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = self.calculator.calculate(num1, num2, operation)
            self.result_label.config(text=str(result))
        except ValueError:
            self.result_label.config(text="ошибка")


def main() -> None:
    """Основная функция, инициализирует и запускает приложение калькулятора."""
    root = tk.Tk()
    root.title("Калькулятор")

    # Создаем экземпляры калькулятора и приложения
    calculator = Calculator()
    app = CalculatorApp(root, calculator)

    # Запуск основного цикла программы
    root.mainloop()
