class KontoBankowe:
    def __init__(self, wlasciciel: str, saldo: float= 0.0):
        self._wlasciciel = wlasciciel
        self._saldo = saldo

    @property
    def wlasciciel(self):
        return self._wlasciciel

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self,kwota: float):
        if kwota <0:
            raise ValueError("Saldo nie może być umjemne!")
        self._saldo = kwota

    @saldo.deleter
    def saldo(self):
        print("saldo zostało wyzerowane")
        self._saldo = 0.0
        # del self._saldo


if __name__ == '__main__':
    konto = KontoBankowe('Jakub')
    print(konto.wlasciciel)
    print(konto.saldo)
    konto.saldo = 100.0
    print(konto.saldo)
    del konto.saldo
    print(konto.saldo)

    try:
        konto.saldo = -1000.0
    except ValueError as e:
        print(e)
