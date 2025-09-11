from dataclasses import dataclass

@dataclass
class Book:
    tytul: str
    autor: str
    strony: int
    cena: float
    rok: int

    def rabat(self, procent: float) -> float:
        """Obniża cenę książki o podany procent i zwraca nową cenę."""
        znizka = self.cena * (procent / 100)
        self.cena -= znizka
        return self.cena


# Tworzymy dwa obiekty
ksiazka1 = Book("Python w praktyce", "Jan Kowalski", 350, 120.00, 2023)
ksiazka2 = Book("Uczenie maszynowe", "Anna Nowak", 500, 150.00, 2021)

# Wypisanie przed rabatem
print("Przed rabatem:")
print(ksiazka1)
print(ksiazka2)

# Zastosowanie rabatu
ksiazka1.rabat(10)   # 10% zniżki
ksiazka2.rabat(25)   # 25% zniżki

# Wypisanie po rabacie
print("\nPo rabacie:")
print(ksiazka1)
print(ksiazka2)
