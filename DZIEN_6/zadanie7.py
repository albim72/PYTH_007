from __future__ import annotations
from dataclasses import dataclass
from math import isqrt
from typing import List


@dataclass
class Analizator:
    """
    Klasa do pracy z listą liczb całkowitych.
    Zawiera metody statyczne, klasowe oraz implementacje sumowania
    iteracyjnego i rekurencyjnego.
    """
    liczby: List[int]

    # 1) Metoda statyczna
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Zwraca True, jeśli n jest liczbą pierwszą, w przeciwnym wypadku False.
        Działa w czasie O(sqrt(n)).
        """
        if n <= 1:
            return False
        if n <= 3:
            return True  # 2 i 3
        if n % 2 == 0 or n % 3 == 0:
            return False
        # testujemy tylko liczby postaci 6k±1
        limit = isqrt(n)
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # 2) Metoda klasowa
    @classmethod
    def from_range(cls, start: int, end: int) -> "Analizator":
        """
        Tworzy obiekt Analizator z liczbami z przedziału [start, end] (obie granice włącznie).
        Jeśli start > end, przedział zostanie zamieniony miejscami.
        """
        if start > end:
            start, end = end, start
        return cls(list(range(start, end + 1)))

    # 3) Funkcja iteracyjna
    def sum_iteracyjnie(self) -> int:
        """
        Zwraca sumę liczb w polu `liczby`, obliczoną iteracyjnie.
        """
        s = 0
        for x in self.liczby:
            s += x
        return s

    # 4) Funkcja rekurencyjna
    def sum_rekurencyjnie(self, idx: int = 0) -> int:
        """
        Zwraca sumę liczb w polu `liczby`, obliczoną rekurencyjnie
        od pozycji `idx` do końca listy.
        """
        if idx >= len(self.liczby):
            return 0
        return self.liczby[idx] + self.sum_rekurencyjnie(idx + 1)

    # Dodatkowo: pomocnicza metoda demonstracyjna
    def primes(self) -> List[int]:
        """Zwraca listę liczb pierwszych z `liczby`."""
        return [x for x in self.liczby if Analizator.is_prime(x)]


def demo() -> dict:
    """
    Uruchamia krótki pokaz działania zgodnie z wymaganiami zadania.
    Zwraca słownik z wynikami.
    """
    analyzer = Analizator.from_range(1, 10)
    primes = analyzer.primes()
    s_iter = analyzer.sum_iteracyjnie()
    s_rec = analyzer.sum_rekurencyjnie()
    assert s_iter == s_rec, "Suma iteracyjna i rekurencyjna powinna być taka sama."
    return {
        "przedzial": analyzer.liczby,
        "pierwsze": primes,
        "suma_iteracyjnie": s_iter,
        "suma_rekurencyjnie": s_rec,
    }


if __name__ == "__main__":
    wyniki = demo()
    print("Przedział:", wyniki["przedzial"])
    print("Liczby pierwsze:", wyniki["pierwsze"])
    print("Suma (iteracyjnie):", wyniki["suma_iteracyjnie"])
    print("Suma (rekurencyjnie):", wyniki["suma_rekurencyjnie"])
