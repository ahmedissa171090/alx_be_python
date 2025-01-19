class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): The book to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title if available.
        
        Args:
            title (str): The title of the book to check out.
        
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return True
        print(f"Book '{title}' is either unavailable or does not exist.")
        return False

    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): The title of the book to return.
        
        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return True
        print(f"Book '{title}' is not checked out or does not exist.")
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
