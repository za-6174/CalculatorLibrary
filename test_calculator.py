"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_division(self):
        assert 3 == calculator.subtract(9, 3)
    
    def test_multiplication(self):
        assert 10 == calculator.subtract(5, 2)