liczby = (5,7,36,24,13,65,43,56,76,54,33,22,43,77,8,13)
print(liczby)
print(type(liczby))

print(liczby[0])
print(liczby[1])
print(liczby[-2])
print(liczby.index(5))
print(liczby.index(56))

print(liczby.count(5))
print(liczby.count(13))

#zastosowwanie-sprawdzenie dostępności miejsca
#lista rezerwacji (rząd, miejsce)

rezerwacje = [(1,5),(2,4),(3,7),(11,8),(21,20)]
print(rezerwacje)

miejsce = (2,4)
if miejsce in rezerwacje:
    print(f"miejsce {miejsce} jest zarezerwowane")
else:
    print(f"miejsce {miejsce} nie jest zarezerwowane")

nb = [43,15,78]
#porzerz krotke liczby o listę nb
liczby = list(liczby)
liczby.extend(nb)
liczby = tuple(liczby)
print(liczby)
