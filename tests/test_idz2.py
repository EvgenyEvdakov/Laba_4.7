#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import sys

sys.path.append('../src')
from idz2 import ColorManager


class TestColorManager(unittest.TestCase):
    """Тесты для класса ColorManager."""

    def setUp(self):
        """Подготовка ColorManager для тестов."""
        self.colors = {
            "Красный": "#ff0000",
            "Оранжевый": "#ff7d00",
            "Желтый": "#ffff00",
            "Зеленый": "#00ff00",
            "Голубой": "#007dff",
            "Синий": "#0000ff",
            "Фиолетовый": "#7d00ff"
        }
        self.color_manager = ColorManager(self.colors)

    def test_get_valid_color_code(self):
        """Тест получения корректного кода цвета."""
        self.assertEqual(self.color_manager.get_color_code("Красный"), "#ff0000")
        self.assertEqual(self.color_manager.get_color_code("Оранжевый"), "#ff7d00")
        self.assertEqual(self.color_manager.get_color_code("Фиолетовый"), "#7d00ff")

    def test_get_invalid_color_code(self):
        """Тест для получения неизвестного цвета."""
        self.assertEqual(self.color_manager.get_color_code("Неизвестный"), "Неизвестный цвет")
        self.assertEqual(self.color_manager.get_color_code("Чёрный"), "Неизвестный цвет")


if __name__ == "__main__":
    unittest.main()