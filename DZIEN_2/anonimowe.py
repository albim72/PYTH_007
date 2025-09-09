#funckje anonimowe
#wykoanie funkcji lambda wewntrz print()
print((lambda a,b: a-b+1)(3,7))

#sortowanie listy po drugiej wartosci w krotce
ocent = [('Kasia', 5), ('Marek', 3), ('Anna', 4)]

#sortujemy po ocenie
posortowane = sorted(ocent, key=lambda x: x[1])
print(posortowane)

#filtrowanie liczb parzystych z listy
liczby = [1, 45, 3, 4, 22, 6, 31, 8, 78, 10]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)

cube = list(map(lambda x: x**3, liczby))
print(cube)
