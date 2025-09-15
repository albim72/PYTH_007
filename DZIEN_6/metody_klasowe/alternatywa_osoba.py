class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def from_string(cls,tekst: str):
        "tworzy obiekt z formatu 'Imie:Wiek' "
        imie, wiek = tekst.split(':')
        return cls(imie, int(wiek))

o1 = Osoba("Leon",45)
o2 = Osoba.from_string("Jakub:12")

print(o1.imie,o1.wiek)
print(o2.imie,o2.wiek)
