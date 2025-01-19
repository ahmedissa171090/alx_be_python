class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize the book attributes
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor to print a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation of the book (for human-readable output)
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation of the book (for debugging and recreation)
        return f"Book('{self.title}', '{self.author}', {self.year})"
