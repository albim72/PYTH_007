imiona = ["Anna","Alicja","Bartek","Andrzej","Karol","Agnieszka"]

def znajdz_i_zamien(imiona):
    wynik = []
    for imie in imiona:
        if imie.startswith("A"):
            wynik.append(imie.upper())
    return wynik

wynik = znajdz_i_zamien(imiona)
print(len(imiona))
print(wynik)
print(len(wynik))
