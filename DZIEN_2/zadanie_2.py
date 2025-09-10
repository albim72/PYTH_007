from __future__ import annotations

def czy_palindrom(slowo: str) -> bool:
    """
    Zwraca True, jeśli 'slowo' jest palindromem (ignorując wielkość liter),
    w przeciwnym wypadku False.
    """
    s = slowo.lower()
    return s == s[::-1]


class BankAccount:
    """
    Prosta symulacja konta bankowego.
    """
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Kwota wypłaty nie może być ujemna.")
        if amount > self.balance:
            print("Za mało środków!")
            return
        self.balance -= amount

    def __str__(self) -> str:
        # Bez miejsc po przecinku, aby dopasować dokładnie format z treści zadania
        if self.balance.is_integer():
            saldo_str = str(int(self.balance))
        else:
            saldo_str = str(self.balance)
        return f"Konto właściciela: {self.owner}, saldo: {saldo_str}"


if __name__ == "__main__":
    # Przykłady użycia dla Zadania 1
    print(czy_palindrom("kajak"))   # True
    print(czy_palindrom("python"))  # False
    print(czy_palindrom("Anna"))    # True

    # Przykłady użycia dla Zadania 2
    konto = BankAccount("Jan", 1000)
    konto.deposit(500)
    print(konto)             # Konto właściciela: Jan, saldo: 1500
    konto.withdraw(2000)     # Za mało środków!
    print(konto)             # Konto właściciela: Jan, saldo: 1500

    konto.withdraw(270)
    print(konto)  
