import re

class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None

print(EmailValidator.is_valid("jan.kowalski@firma.pl"))
print(EmailValidator.is_valid("bad.email@com"))

"""
pattern --> To jest wyrażenie regularne (regex), które najczęściej używa się do prostego sprawdzenia, czy coś wygląda jak adres e-mail. Teraz krok po kroku:

1. r"..."

Przedrostek r oznacza raw string w Pythonie. Dzięki temu backslashy (\) nie trzeba podwójnie uciekać.
Np. "\n" to nowa linia, ale r"\n" to po prostu dwa znaki: backslash i n.

2. [^@]+

[...] – klasa znaków (pasuje do jednego z podanych znaków).

^ na początku w środku nawiasów kwadratowych oznacza negację.

[^@] – pasuje do każdego znaku oprócz znaku @.

+ – oznacza jeden lub więcej wystąpień.

Czyli [^@]+ = „ciąg co najmniej jednego znaku, który nie jest @”.

3. @

Po tym ciągu musi pojawić się dosłowny znak @.
To rozdziela część użytkownika (np. jan.kowalski) od domeny (np. gmail.com).
"""
