# File: oop/library_system.py

"""Library system using inheritance and composition."""


class Book:
    def __init__(self, title, author):
        """Initialize Book with title and author."""
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with inherited and unique attributes."""
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with inherited and unique attributes."""
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books."""
        for book in self.books:
            print(book.get_info())
