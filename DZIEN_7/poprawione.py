class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = 0.0
        self.price = price  # walidacja przez setter

    @property
    def price(self):
        return self._price  # poprawka: brak rekursji

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Cena nie może być ujemna.")
        self._price = float(value)

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price:.2f})"


class Member:
    def __init__(self, name, borrowed=None):
        self.name = name
        self.borrowed = [] if borrowed is None else list(borrowed)  # brak mutowalnego domyślnego

    def borrow(self, book: Book):
        self.borrowed.append(book)

    def __repr__(self):
        return f"Member(name={self.name!r}, borrowed={[b.title for b in self.borrowed]})"


class Library:
    def __init__(self):
        self.books = {}  # title -> Book

    def add_book(self, book: Book):
        self.books[book.title] = book

    def lend(self, title: str, member: Member):
        book = self.books.pop(title, None)
        if book is None:
            print("Brak książki!")
            return
        member.borrow(book)  # przekazujemy obiekt Book, nie string


# --- krótki test działania ---
if __name__ == "__main__":
    lib = Library()
    b1 = Book("Python 101", "A. Author", 50)  # popraw
    print(b1)

"""
Lista błędów do poprawy
Book.__init__ pozwala na ujemną cenę (brak walidacji).
Book.price getter robi rekursję (powinien zwrócić self._price).
Member.__init__ używa mutowalnej listy jako argumentu domyślnego (wszyscy członkowie dzielą tę samą listę).
Library.lend dodaje do borrowed tytuł (string), zamiast obiektu Book.
W kodzie testowym tworzona jest książka z ujemną ceną, która powinna rzucić wyjątek.
"""
