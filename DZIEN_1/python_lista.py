# tworzenie listy
"""
pierwszy komentarz wieloliniowy-dokumentacyjny (i tylko pierwszy)
podstawowe działania na lisatch
tworzenie
dodawanie elementów
usuwanie elementów
sortoeanie i inne
"""

# def nazwa():
#     """
#     dokuemtacja
#     :return:
#     """
#     pass

# CTRL + /  -> komentowanie/odkomentowanie bloków kodu
# CTRL + D -> duplikacja bloków kodu

from statistics import stdev

studenci = ["Ala", "Bartek", "Leon", "Lidia", "Marek", "Ewa", "Ala"]
oceny = [5, 5, 4, 3, 3, 2, 5]
mieszana = ["Toruń", 434.4, True, 3, "Ala", [5, 3, 6]]

print(studenci)
print(type(studenci))

print(oceny)
print(type(oceny))

print(mieszana)
print(type(mieszana))

print("_" * 70)
print("PLASTERKOWANIE")
print(studenci[0])
print(studenci[4])
print(studenci[3:])
print(studenci[:6])
print(studenci[-2])

print("dodawanie do listy")
studenci.append("Kasia")
print(studenci)

studenci.insert(3, "Marian")
print(studenci)

studenci.remove("Leon")
print(studenci)

while "Leon" in studenci:
    studenci.remove("Leon")

print(studenci)

if "Olaf" in studenci:
    studenci.remove("Olaf")
else:
    print("Nie ma Olafa")

print(studenci)

# usuwanie po indeksie
del studenci[2]
print(studenci)

usuniety = studenci.pop(3)
print(studenci)
print(usuniety)

# iteracja po liście
for i, v in enumerate(studenci):  # funkcja enumerate zwraca zwsze parę danych: pierwsza-indeks, druga-wartość
    print(f"indeks: {i} -> wartość: {v}")

#łączenie list
nowa = ["Hubert","Iza"]
studenci.extend(nowa)
print(studenci)

kolejni = ["Justyna","Ula","Marcin"]
studenci = studenci + kolejni
print(studenci)

#list comprehension
kwadraty = [x**2 for x in range(1,13)]
print(kwadraty)

oceny_pow_3 = [oc for oc in oceny if oc>3]
print(oceny_pow_3)

#sortowanie elementów
print("sortowanie")
print(f"studenci: {sorted(studenci)}")
print(f"studenci odrotnie: {sorted(studenci,reverse=True)}")

studenci.sort()
print(studenci)

#listy złożone
print("______ listy wielowymiarowe _______")
tabela = [
    ["Ala",5],
    ["Józef",5],
    ["Nadia",3],
    ["Olaf",3],
    ["Piotr",4],
    ["Bronka",4],
    ["Wiesław",5],

]

for imie,ocena in tabela:
    print(f"{imie} -> {ocena}")
print("_"*70)
print(f"ocena najwyższa: {max(tabela,key=lambda x:x[1])}")
print(f"ocena najniższa: {min(tabela,key=lambda x:x[1])}")

print("inaczej....")
ocn = [x[1] for x in tabela]
print(f"lista ocen: {ocn}")

print(f"ocena najwyższa: {max(ocn)}")
print(f"ocena najniższa: {min(ocn)}")

print(f"średnia oceny: {sum(ocn)/len(ocn):.2f}")
print(f"odchylenie standardowe: {stdev(ocn):.2f}")








