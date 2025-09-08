#tworzenie listy
"""
pierwszy komentarz wieloliniowy - dokumentacyjny (i tylko pierwszy)
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

#CTRL + /  -> komentowanie/odkomentowanie bloków kodu
#CTRL + D -> duplikacja bloków kodu

studenci = ["Ala","Bartek","Leon","Lidia","Marek","Ewa","Ala"]
oceny = [5,5,4,3,3,2,5]
mieszana = ["Toruń",434.4,True,3,"Ala",[5,3,6]]

print(studenci)
print(type(studenci))

print(oceny)
print(type(oceny))

print(mieszana)
print(type(mieszana))

print("_"*70)
print("PLASTERKOWANIE")
print(studenci[0])
print(studenci[4])
print(studenci[3:])
print(studenci[:6])
print(studenci[-2])

print("dodawanie do listy")
studenci.append("Kasia")
print(studenci)

studenci.insert(3,"Marian")
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

#usuwanie po indeksie
del studenci[2]
print(studenci)

usuniety = studenci.pop(3)
print(studenci)
print(usuniety)


