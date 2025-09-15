class KontoBankowe:
    def __init__(self, wlasciciel: str, saldo: float=0.0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    @classmethod
    def konto_premium(cls,wlasciciel: str):
        """tworzy konto premium z 10000.0 bonusu na start"""
        return cls(wlasciciel, 10000.0)


zwykle = KontoBankowe("Marek",500)
premium = KontoBankowe.konto_premium("Ewa")

print(zwykle.wlasciciel,zwykle.saldo)
print(premium.wlasciciel,premium.saldo)    
