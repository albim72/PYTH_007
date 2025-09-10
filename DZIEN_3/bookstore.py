class Book:
    __kolor = "czerwony" #private
    grubosc = 3
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(Book)

    def __init__(self, title, author, price, pages, bookstore_nb):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.bookstore_nb = bookstore_nb
        self.binding = "miękka"
        self.newbook()

    def __repr__(self):
        return f"{self.title} by {self.author}, binding: {self.binding}"

    def newbook(self):
        print("Nowy obiekt klasy Book!")

    def get_binding(self):
        return self.binding

    def set_binding(self,binding):
        self.binding = binding

    def cena_rabat(self,procent):
        self.price = self.price - (self.price * procent/100)
        return self.price

    def obwoluta(self):
        return self.__kolor



if __name__ == '__main__':
    b1 = Book("ABC biegacza ultra","Jurek Scott",102,345,22)
    print(b1)
    #to nie jest najlepsza droga do operwoania na zmiennej binding!
    # print(b1.binding)
    # b1.binding = "twarda"
    # print(b1.binding)

    print(b1.get_binding())
    b1.set_binding("twarda")
    print(b1.get_binding())
    print(b1)
    print(b1.cena_rabat(12))

    b2 = Book("Python AI","Marcin Albiniak",99,435,1)
    print(b2)
    print(b2.cena_rabat(17))

    print("____ zmienne klasy _____")
    print(Book.grubosc)
    print(b1.grubosc)
    # print(b1.__kolor)
    print(b1.obwoluta())
