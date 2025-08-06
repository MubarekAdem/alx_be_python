# File: oop/polymorphism_demo.py

"""Polymorphism demo with Shape base class and area() method."""

import math


class Shape:
    def area(self):
        """Raise error if area is not implemented in subclass."""
        raise NotImplementedError("Subclasses must override area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2
