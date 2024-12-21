#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import sys
import unittest

sys.path.append('../src')
from idz5 import ContactApp

class TestContactApp(unittest.TestCase):
    def setUp(self):
        """Создаем тестовое приложение перед каждым тестом."""
        self.root = tk.Tk()
        self.contacts = {
            "Имя": "Евгений",
            "Фамилия": "Евдаков",
            "Отчество": "Владимирович"
        }
        self.app = ContactApp(self.root, self.contacts)

    def tearDown(self):
        """Закрываем окно приложения после теста."""
        self.root.destroy()

    def test_initial_state(self):
        """Проверяем начальное состояние приложения."""
        self.assertEqual(self.app.selected_contact.get(), "")
        self.assertEqual(self.app.info_label.cget("text"), "")

    def test_show_info(self):
        """Тестируем метод show_info."""
        self.app.show_info("Имя")
        self.assertEqual(self.app.info_label.cget("text"), "Евгений")

        self.app.show_info("Фамилия")
        self.assertEqual(self.app.info_label.cget("text"), "Евдаков")

        self.app.show_info("Отчество")
        self.assertEqual(self.app.info_label.cget("text"), "Владимирович")

    def test_radiobutton_selection(self):
        """Проверяем выбор радиокнопки."""
        self.app.selected_contact.set("Имя")
        self.app.show_info("Имя")
        self.assertEqual(self.app.info_label.cget("text"), "Евгений")

        self.app.selected_contact.set("Фамилия")
        self.app.show_info("Фамилия")
        self.assertEqual(self.app.info_label.cget("text"), "Евдаков")

if __name__ == "__main__":
    unittest.main()