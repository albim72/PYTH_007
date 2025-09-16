# Zadanie: Znajdź i popraw 5 błędów w kodzie!
# Cel: stworzyć prosty system biblioteki z książkami i czytelnikiem.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = price  # BUG 1: brak walidacji ujemnej ceny

    @property
    def price(self):
        return self.price  # BUG 2: nieskończona rekursja!

    @price.setter
    def price(self, value):
        self._price = value

class Member:
    def __init__(self, name, borrowed=[]):  # BUG 3: mutowalny argument domyślny
        self.name = name
        self.borrowed = borrowed

    def borrow(self, book):
        self.borrowed.append(book)

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def lend(self, title, member):
        if title in self.books:
            member.borrow(title)  # BUG 4: dodaje string zamiast obiektu Book
            del self.books[title]
        else:
            print("Brak książki!")

# Program testowy
lib = Library()
b1 = Book("Python 101", "A. Author", -50)  # BUG 5: cena ujemna, a nie zgłasza błędu
m1 = Member("Anna")

lib.add_book(b1)
lib.lend("Python 101", m1)

print(m1.borrowed)
