def odwroc_rekurencyjnie(tekst: str) -> str:
    if len(tekst) <= 1:  # warunek końcowy
        return tekst
    return odwroc_rekurencyjnie(tekst[1:]) + tekst[0]


# Test
print(odwroc_rekurencyjnie("Python"))  # nohtyP


def odwroc_iteracyjnie(tekst: str) -> str:
    wynik = ""
    for znak in tekst:
        wynik = znak + wynik  # doklejanie na początek
    return wynik


# Test
print(odwroc_iteracyjnie("Python"))  # nohtyP

#idea rezonansowa
def echo_rekurencyjne(tekst: str) -> str:
    if len(tekst) <= 1:  # punkt skupienia fali
        return tekst
    return tekst[-1] + echo_rekurencyjne(tekst[1:-1]) + tekst[0]


print(echo_rekurencyjne("Synapse"))  # esnapyS

class EchoRezonansowe:
    """
    Echo falowe (rezonansowe) odwracanie napisu.

    Archetypy:
    - left  -> Inicjator (początek)
    - right -> Cień (koniec)
    - środek -> Oś / Centrum (gdy left == right)
    """

    def echo(self, tekst: str) -> str:
        """API publiczne — zwraca 'echo' (odwrócony napis) w trybie falowym."""
        return self._echo_rekurencyjne(tekst, 0, len(tekst) - 1)

    def _echo_rekurencyjne(self, s: str, left: int, right: int) -> str:
        # Base cases (warunki końcowe)
        if left > right:           # pusta szczelina (parzysta długość)
            return ""
        if left == right:          # Centrum / Oś (nieparzysta długość)
            return s[left]

        # Rezonans brzegów: Cień (right) ↔ Inicjator (left), schodzimy do wnętrza
        return s[right] + self._echo_rekurencyjne(s, left + 1, right - 1) + s[left]


# ✅ Przykład użycia
e = EchoRezonansowe()
print(e.echo("Synapse"))   # esnapyS
print(e.echo("ANIMA"))     # AMINA
print(e.echo("Rezonans"))  # snanozeR

# ✅ Szybkie asercje
assert e.echo("abc")   == "cba"
assert e.echo("abba")  == "abba"[::-1]
assert e.echo("x")     == "x"
assert e.echo("")      == ""

