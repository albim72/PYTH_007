class Konto:
    licznik = 0
    def __init__(self, wlasciciel: str):
        self.wlasciciel = wlasciciel
        Konto.licznik += 1

    @classmethod
    def ile_kont(cls):
        return cls.licznik

k1 = Konto("Jakub")
k2 = Konto("Maria")
k3 = Konto("Anna")
print(Konto.ile_kont())
