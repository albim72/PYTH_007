class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} i mam {self.wiek} lat.")
