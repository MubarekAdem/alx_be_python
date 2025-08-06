# File: oop/book_class.py

"""Book class demonstrating magic methods."""

class Book:
    def __init__(self, title, author, year):
        """Initialize Book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print message when a Book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
