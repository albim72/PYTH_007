imiona = ["Anna","Alicja","Bartek","Andrzej","Karol","Agnieszka"]

def znajdz_i_zamien(imiona):
    wynik = []
    for imie in imiona:
        if imie.startswith("A"):
            wynik.append(imie.upper())
    return wynik

wynik_c = znajdz_i_zamien(imiona)
print(len(imiona))
print(wynik_c)
print(len(wynik_c))

#przypadek 2
print("________ przypadek modyfikacji globalnej _________")
wynik2 = []
def znajdz_i_zamien2(imiona):
    for imie in imiona:
        if imie.startswith("A"):
            wynik2.append(imie.upper())

znajdz_i_zamien2(imiona)
print(len(imiona))
print(wynik2)
print(len(wynik2))

wynik2.append("Leon")
print(wynik2)

wynik.append("Tomasz")
print(wynik)

