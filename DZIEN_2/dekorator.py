#deklaracja dekoratora
#przypadek 1: prosty przykład
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
