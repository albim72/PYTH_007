"""
opiszemy grupę funckji
pokażemy różne aspekty wykorzystania funckji w Pythonie
"""

#prosta funkcja bez argumentów
def powitanie():
    print("Witaj w świecie Pythona!")

#funkcja z jednym argumentem
def kwadrat(x):
    return x**2

#funkcja z dwoma argumentami
def suma(a,b):
    return a+b

#funkcja z wartością domyślną
def powitanie_uzytkownika(imie,jezyk="PL"):
    if jezyk=="PL":
        print(f"Witaj na pokładzie {imie}!")
    elif jezyk == "EN":
        print(f"Welcome to Python world {imie}!")
    else:
        print(f"Hello/Witaj {imie}! I'm Python!/Jestem Pythonem!")

#funkcja zwracająca wiele wartości
def dzielenie(a,b):
    """
    zwraca (iloraz całkowity, reszta) dla liczb całkowitych a,b
    :param a: int
    :param b: int
    :return: divmod(a,b)
    """
    if b==0:
        raise ZeroDivisionError("Nie dziel przez zero!")
    return divmod(a,b)

#funkcja z listą jako argumentem
def srednia(lista: list) -> float:
    if not lista:
        raise ValueError("lista pusta!")
    return sum(lista)/len(lista)


if __name__ == '__main__':
    print("__________ funkcja powitanie ___________")
    powitanie()
    print("__________ funkcja kwadrat ___________")
    print(kwadrat(5))
    print(kwadrat(-3))
    print(kwadrat(1.567))
    z = kwadrat(4)
    print(z)
    print("__________ funkcja suma ___________")
    print(suma(1,2))
    print(suma(1.5,2.5))
    print(suma(-1,-2))
    print("__________ funkcja powitanie_uzytkownika ___________")
    powitanie_uzytkownika("Marek")
    powitanie_uzytkownika("Marek", "PL")
    powitanie_uzytkownika("Anna", "EN")
    powitanie_uzytkownika("Lana", "FR")
    print("__________ funkcja dzielenie ___________")
    try:
        iloraz,reszta = dzielenie(10,5)
        print(f"dzielenie(10,5) -> iloraz: {iloraz}, reszta: {reszta}")
        iloraz, reszta = dzielenie(6, 5)
        print(f"dzielenie(6,5) -> iloraz: {iloraz}, reszta: {reszta}")
        iloraz, reszta = dzielenie(-3, 0)
        print(f"dzielenie(-3,0) -> iloraz: {iloraz}, reszta: {reszta}")
    except ZeroDivisionError as e:
        print(e)
    print("__________ funkcja srednia ___________")
    print(f"srednia([1,2,3,4,5]) -> {srednia([1,2,3,4,5]):.2f}")
    print(f"srednia([1,2,34,7,90,3,-34,25,68]) -> {srednia([1,2,34,7,90,3,-34,25,68]):.2f}")
    try:
        print(f"srednia([]) -> {srednia([]):.2f}")
    except ValueError as e:
        print(e)
