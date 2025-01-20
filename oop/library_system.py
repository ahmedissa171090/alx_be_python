class Book:
    def __init__(self, title, author):
        # Initialize common attributes for all books
        self.title = title
        self.author = author

    def __str__(self):
        # String representation for a generic book
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor and initialize specific attributes
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # String representation for an EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor and initialize specific attributes
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # String representation for a PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book):
        # Add a book instance to the library
        self.books.append(book)

    def list_books(self):
        # Print details of each book in the library
        for book in self.books:
            print(book)
