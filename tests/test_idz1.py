#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('../src')
from idz1 import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calculate(5, 3, "+"), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calculate(5, 3, "-"), 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calculate(5, 3, "*"), 15)

    def test_division(self):
        self.assertEqual(self.calculator.calculate(6, 3, "/"), 2)

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.calculate(6, 0, "/"), "ошибка")

    def test_invalid_operation(self):
        self.assertEqual(self.calculator.calculate(6, 3, "%"), "ошибка")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calculator.calculate("a", 3, "+")

        with self.assertRaises(TypeError):
            self.calculator.calculate(5, "b", "-")

        with self.assertRaises(TypeError):
            self.calculator.calculate("a", "b", "*")


if __name__ == "__main__":
    unittest.main()