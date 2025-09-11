try:
    #kod krtóry może wywołać wyjątek
    liczba = int(input("Podaj liczbę: "))
    wynik = 10/liczba
except ValueError:
    #ValueError wykona się tylko wtedy gdy błędem będzie wpisanie str
    print("To nie jest liczba!")
except ZeroDivisionError:
    #ZeroDivisionError wykona się tylko wtedy gdy liczba = 0
    print("Nie dziel przez zero!")
else:
    #else wykonuje się tylko wtedy jak try wykona się bez błędów!
    print(f"Wynik: {wynik}")
finally:
    #finally wykonuje się zawsze
    print("Koniec programu!")
