class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, pages):
        self.books.append((title, author, pages))

    def show_books(self):
        for book in self.books:
            print(book)

    @property
    def total_pages(self):

        total_pages = 0

        for title, author, pages in self.books:
            total_pages += pages

        return total_pages
    
    @property
    def longest_book(self):

        longest_book = self.books[0]

        for title, author, pages in self.books:
            if pages > longest_book[2]:
                longest_book = (title, author, pages)

        return longest_book
    
    def __str__(self):
        return f"This library has {len(self.books)} books."
    

library1 = Library()

library1.add_book("Babel", "R.F. Kuang", 500)
library1.add_book("Heather", "Kyle A. Vanderbilt", 40)
library1.add_book("Red", "Maky T. Salo", 324)
library1.add_book("Hey, Anne", "Doglass", 213)

library1.show_books()
print(library1.total_pages)
print(library1.longest_book)
print(library1)
