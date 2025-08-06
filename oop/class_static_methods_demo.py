# File: oop/class_static_methods_demo.py

"""Demonstration of class methods vs static methods."""


class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of a and b and print calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
