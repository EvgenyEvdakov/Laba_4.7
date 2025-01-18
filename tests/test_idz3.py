#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


sys.path.append("../src")
from idz3 import ColorManager


class TestColorManager(unittest.TestCase):
    """Тесты для класса ColorManager."""

    def setUp(self):
        """Подготовка данных для тестов."""
        self.colors = {
            "красный": "#ff0000",
            "оранжевый": "#ff7f00",
            "желтый": "#ffff00",
            "зеленый": "#00ff00",
            "голубой": "#00ffff",
            "синий": "#0000ff",
            "фиолетовый": "#7f00ff",
        }
        self.color_manager = ColorManager(self.colors)

    def test_get_valid_color_code(self):
        """Тест получения корректного кода цвета."""
        self.assertEqual(self.color_manager.get_color_code("красный"), "#ff0000")
        self.assertEqual(self.color_manager.get_color_code("желтый"), "#ffff00")
        self.assertEqual(self.color_manager.get_color_code("фиолетовый"), "#7f00ff")

    def test_get_invalid_color_code(self):
        """Тест получения неизвестного цвета."""
        self.assertEqual(self.color_manager.get_color_code("неизвестный"), "#ffffff")  # Белый по умолчанию


if __name__ == "__main__":
    unittest.main()
