drzewa = {"jodła","dąb","buk","jabłoń","olcha","dąb"}
print(drzewa)
print(drzewa)
print(drzewa)

drzewa.add("wierzba")
print(drzewa)

drzewa.remove("olcha")
print(drzewa)

drzewa.discard("machoń")

#sortowanie konwersja na listę
dr = list(drzewa)
dr.sort()
print(dr)

#uczestnicy warsztatów ceramiki
warsztat1 = ["Ala","Bartek","Celina","Ala","Darek","Urszula","Tomasz"]
warsztat2 = ["Celina","Ewa","Filip","Bartek","Filip","Tomasz","Euzebiusz"]

#zamina  list na  zbiory
ucz1 = set(warsztat1)
ucz2 = set(warsztat2)

print(ucz1)
print(ucz2)

#kto brał udział w obu warsztatach na raz
print(ucz1.intersection(ucz2))

#ile fizcznie osób uczestniczyło w obu warsztatach
print(len(ucz1.union(ucz2)))

wszyscy = ucz1 | ucz2
print(wszyscy)

#kto był tylko na 1 warsztacie?
pierwszy = ucz1 - ucz2
print(pierwszy)

#zbiór zamrożony
zam = frozenset(wszyscy)
print(zam)


zam.add("Grzegorz")
