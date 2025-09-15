class KontoBankowe:
    def __init__(self, wlasciciel: str, saldo: float = 0.0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplata(self,kwota: float):
        self.saldo += kwota
        print(f"{self.wlasciciel} wpłacił {kwota}. Nowe saldo: {self.saldo}")

    def wyplata(self,kwota: float):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f"{self.wlasciciel} wypłacił {kwota}. Nowe saldo: {self.saldo}")
        else:
            print(f"Nie ma takiej kwoty na koncie {self.saldo}")

    def nalicz_odsetki(self,oprocentowanie:float,lata:int):
        odsetki = KontoBankowe.oblicz_odsetki(self.saldo,oprocentowanie,lata)
        self.saldo -= odsetki
        print(f"naliczono odsetki: {odsetki}. Saldo: {self.saldo}")

    @staticmethod
    def oblicz_odsetki(kwota:float,oprocentowanie:float,lata: int):
        return kwota * ((1+oprocentowanie)**lata-1) #procent składany

konto = KontoBankowe("Jan")
konto.wplata(1500)
konto.wyplata(1200)
konto.nalicz_odsetki(0.02,1)

