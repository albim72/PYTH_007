from datetime import datetime
from statistics import mean

print("\n" + "=" * 72)
print("1) LISTA (list)")
print("=" * 72)

# Utwórz listę imion uczniów w klasie
uczniowie = ["Ala", "Olaf", "Karol", "Maria", "Ela"]
print(f"Początkowa lista uczniów: {uczniowie}")

# Dodaj kilku uczniów do listy
uczniowie.extend(["Bartek", "Zosia"])
print(f"Po dodaniu nowych osób: {uczniowie}")

# Usuń jednego ucznia
usuniety = uczniowie.pop(2)  # np. usuwamy „Karol”
print(f"Usunięto: {usuniety}")
print(f"Aktualna lista: {uczniowie}")

# Wyświetl wszystkich uczniów wraz z numerem porządkowym
print("Lista z numerami porządkowymi:")
for i, imie in enumerate(uczniowie, start=1):
    print(f"{i}. {imie}")


print("\n" + "=" * 72)
print("2) KROTKA (tuple)")
print("=" * 72)

uczen = ("Ala", "Kowalska", 2010)
print(f"Przykładowa krotka ucznia: {uczen}")
print(f"Rok urodzenia: {uczen[2]}")

try:
    uczen[2] = 2011  # próba zmiany (powinna dać błąd)
except TypeError as e:
    print("Próba modyfikacji krotki zakończona błędem:")
    print(f"TypeError: {e}")


print("\n" + "=" * 72)
print("3) ZBIORY (set / frozenset)")
print("=" * 72)

kolo_matematyczne = {"Ala", "Olaf", "Maria", "Zosia"}
kolo_sportowe     = {"Bartek", "Olaf", "Ela", "Zosia", "Kamil"}

print(f"Koło matematyczne: {kolo_matematyczne}")
print(f"Koło sportowe    : {kolo_sportowe}")

oba_kola = kolo_matematyczne & kolo_sportowe
print(f"Uczniowie na obu kołach: {oba_kola}")

tylko_sport = kolo_sportowe - kolo_matematyczne
print(f"Tylko sportowe: {tylko_sport}")

unikalni = kolo_matematyczne | kolo_sportowe
print(f"Wszyscy unikalni: {unikalni}")

kolo_matematyczne_immutable = frozenset(kolo_matematyczne)
print(f"Koło matematyczne (frozenset): {kolo_matematyczne_immutable}")

try:
    kolo_matematyczne_immutable.add("Karol")
except AttributeError as e:
    print("Próba dodania do frozenset zakończona błędem:")
    print(f"AttributeError: {e}")


print("\n" + "=" * 72)
print("4) SŁOWNIK (dict)")
print("=" * 72)

oceny = {
    "Ala":   [5, 4, 3],
    "Bartek":[3, 3, 4],
    "Ela":   [4, 4, 5]
}
print(f"Początkowe oceny: {oceny}")

oceny["Olaf"] = [5, 5, 4]
print("Po dodaniu Olaf:", oceny)

oceny["Ala"].append(5)
print("Po dopisaniu oceny Ali:", oceny)

print("Średnie ocen:")
for imie, lista_ocen in oceny.items():
    sr = mean(lista_ocen) if lista_ocen else 0.0
    print(f"{imie} → {sr:.2f}")


print("\n" + "=" * 72)
print("ZADANIE DODATKOWE")
print("=" * 72)

uczniowie_info = {
    "Ala":   ("Kowalska", 2010),
    "Bartek":("Nowak",    2009),
    "Ela":   ("Wiśniewska",2011),
    "Olaf":  ("Zieliński", 2010),
    "Zosia": ("Kaczmarek", 2009),
}
print("Dane uczniów:")
for imie, (nazw, rok) in uczniowie_info.items():
    print(f"{imie} → ({nazw}, {rok})")

rok_biezacy = datetime.now().year
wiek = [rok_biezacy - rok for (_, rok) in uczniowie_info.values()]
sredni_wiek = mean(wiek) if wiek else 0.0

print(f"\nRok bieżący: {rok_biezacy}")
print(f"Wiek uczniów: {wiek}")
print(f"Średni wiek uczniów: {sredni_wiek:.2f} lat")
