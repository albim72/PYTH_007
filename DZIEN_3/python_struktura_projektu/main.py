# import dane
# import dane as dn
import math
import copy

from dane import liczby,leader,MC as m,kolor
from mfunkcje.kwadraty import kwadrat,parzyste,slownik
from mojpakiet import Osoba


print("_"*60)
print(f"liczby -> {liczby}")
print("_"*60)
print(f"słownik leader -> {leader}")
print("_"*60)
# print(f"stala MC = {MC}")
print(f"stala MC = {m}")
MC = "listopad"
print(f"stala MC = {m}")
print(f"stala MC = {MC}")
print("_"*60)
print(f"sin(121) = {math.sin(121)}")
lb = copy.deepcopy(liczby) #kopia głęboka tworzy nowy obiket typu zadanego z uwzględnieniem zgnieżdzeń
print(f"liczby -> {lb}")
print(lb is liczby)
print(f"kwadrat(lb) -> {kwadrat(lb)}")
print(f"parzyste(lb) -> {parzyste(lb)}")
print(f"slownik(leader) -> {slownik(leader)}")
print("_"*60)

jan = Osoba("Jan",32)
jan.przedstaw_sie()
