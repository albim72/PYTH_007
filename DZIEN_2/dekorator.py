#deklaracja dekoratora
#przypadek 1: prosty przykład
import time

def dekorator(funkcja):
    def wrapper():
        print("to jest początek....")
        funkcja()
        print("... to jest koniec!")
    return wrapper

@dekorator
def powitanie():
    print("witaj w świecie dekoratorów!")

powitanie()

print("_"*80)

def mierzenie_czasu(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania funkcji to {end-start} sekund.")
        return wynik
    return wrapper

@mierzenie_czasu
def suma_duzej_listy():
    return sum(range(100_000_000))

print(suma_duzej_listy())

@mierzenie_czasu
def big_suma():
    return sum([a+b*c for (a,b,c) in zip(range(100_000_000), range(100_000_000), range(100_000_000))])

print(big_suma())
