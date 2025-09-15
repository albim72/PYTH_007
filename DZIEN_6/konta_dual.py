class KontoBankowe:
    wszystkie_konta = []  # lista obiektów, wspólna dla klasy

    def __init__(self, wlasciciel: str, saldo: float = 0.0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        KontoBankowe.wszystkie_konta.append(self)

    # metoda obiektowa
    def nalicz_odsetki(self, oprocentowanie: float, lata: int):
        odsetki = KontoBankowe.oblicz_odsetki(self.saldo, oprocentowanie, lata)
        self.saldo += odsetki
        print(f"📈 {self.wlasciciel}: naliczono odsetki {odsetki}, nowe saldo = {self.saldo}")

    # metoda statyczna
    @staticmethod
    def oblicz_odsetki(kwota: float, oprocentowanie: float, lata: int) -> float:
        """Procent składany"""
        return kwota * ((1 + oprocentowanie) ** lata - 1)

    # metoda klasowa
    @classmethod
    def konto_premium(cls, wlasciciel: str):
        """Tworzy konto premium z początkowym saldem 10 000"""
        return cls(wlasciciel, saldo=10000)

    @classmethod
    def liczba_kont(cls):
        """Zwraca liczbę wszystkich utworzonych kont"""
        return len(cls.wszystkie_konta)


# Użycie
k1 = KontoBankowe("Jan", 1000)           # zwykłe konto
k2 = KontoBankowe.konto_premium("Anna")  # konto premium

k1.nalicz_odsetki(0.05, 2)  # używa metody statycznej wewnątrz metody obiektowej
k2.nalicz_odsetki(0.03, 3)

print("Liczba wszystkich kont:", KontoBankowe.liczba_kont())
