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
