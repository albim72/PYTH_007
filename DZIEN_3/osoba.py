class Osoba:
    def __init__(self, imie, nazwisko, miasto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miasto = miasto

    @property
    def miasto(self):
        return self._miasto

    @miasto.setter
    def miasto(self, miasto):
        self._miasto = miasto


if __name__ == '__main__':
    osoba = Osoba('Jan', 'Kowalski', 'Warszawa')
    print(osoba.miasto)
    osoba.miasto = 'Poznań'
    print(osoba.miasto)
