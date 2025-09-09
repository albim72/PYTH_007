#definicja najprostszej klasy
class Samochod:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model

auto = Samochod("BMW","5")
print(auto.marka)
print(auto.model)

#metoda w klasie
class Prostokat:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def pole(self):
        return self.a*self.b

p = Prostokat(2,3)
print(p.pole())

#dziedziczenie
class Zwierze:
    def __init__(self,imie):
        self.imie=imie

    def dzwiek(self):
        return "???"

class Kot(Zwierze):
    def __init__(self,imie,umaszczenie):
        super().__init__(imie)
        self.umaszczenie=umaszczenie

    def dzwiek(self):
        return "Miau!"

class Pies(Zwierze):
    def __init__(self,imie,rasa):
        super().__init__(imie)
        self.rasa=rasa

    def dzwiek(self):
        return "Hau!"

pies = Pies("Ludvik","Buldog angielski")
print(pies.dzwiek())

kot = Kot("Kot","jasne")
print(kot.dzwiek())

pies = Pies("Roman","Owczarek belgijski")
print(pies.dzwiek())

