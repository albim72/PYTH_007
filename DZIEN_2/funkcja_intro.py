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
