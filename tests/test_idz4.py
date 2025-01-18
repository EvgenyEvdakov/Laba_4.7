#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
from unittest.mock import mock_open, patch


sys.path.append("../src")
from idz4 import FileManager


class TestFileManager(unittest.TestCase):
    """Тесты для класса FileManager."""

    def setUp(self):
        """Подготовка данных для тестов."""
        self.file_manager = FileManager()

    @patch("builtins.open", new_callable=mock_open, read_data="test content")
    def test_open_file_success(self, mock_file):
        """Тест успешного открытия файла."""
        content = self.file_manager.open_file("test.txt")
        self.assertEqual(content, "test content")
        mock_file.assert_called_once_with("test.txt", "r", encoding="utf-8")

    @patch("tkinter.messagebox.showerror")
    def test_open_file_not_found(self, mock_messagebox):
        """Тест открытия несуществующего файла."""
        content = self.file_manager.open_file("nonexistent.txt")
        self.assertIsNone(content)
        mock_messagebox.assert_called_once_with("Ошибка", "Файл nonexistent.txt не найден!")

    @patch("tkinter.messagebox.showerror")
    @patch("builtins.open", side_effect=PermissionError("Permission denied"))
    def test_open_file_permission_error(self, mock_file, mock_messagebox):
        """Тест ошибки прав доступа при открытии файла."""
        content = self.file_manager.open_file("test.txt")
        self.assertIsNone(content)
        mock_messagebox.assert_called_once_with("Ошибка", "Не удалось открыть файл: Permission denied")

    @patch("builtins.open", new_callable=mock_open)
    @patch("tkinter.messagebox.showinfo")
    def test_save_file_success(self, mock_messagebox, mock_file):
        """Тест успешного сохранения файла."""
        self.file_manager.save_file("test.txt", "new content")
        mock_file.assert_called_once_with("test.txt", "w", encoding="utf-8")
        mock_file().write.assert_called_once_with("new content")
        mock_messagebox.assert_called_once_with("Успех", "Файл test.txt успешно сохранен!")

    @patch("tkinter.messagebox.showerror")
    @patch("builtins.open", side_effect=PermissionError("Permission denied"))
    def test_save_file_permission_error(self, mock_file, mock_messagebox):
        """Тест ошибки прав доступа при сохранении файла."""
        self.file_manager.save_file("test.txt", "new content")
        mock_messagebox.assert_called_once_with("Ошибка", "Не удалось сохранить файл: Permission denied")


if __name__ == "__main__":
    unittest.main()
