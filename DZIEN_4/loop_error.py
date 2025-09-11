while True:
    try:
        # kod krtóry może wywołać wyjątek
        dane = input("Podaj liczbę lub  wpisz exit - jeśli chcesz opuścić program: ")
        if dane.lower() == "exit":
            print("koniec działania programu")
            break
        liczba = int(dane)
        wynik = 10 / liczba
    except ValueError:
        # ValueError wykona się tylko wtedy gdy błędem będzie wpisanie str
        print("To nie jest liczba!")
    except ZeroDivisionError:
        # ZeroDivisionError wykona się tylko wtedy gdy liczba = 0
        print("Nie dziel przez zero!")
    else:
        # else wykonuje się tylko wtedy jak try wykona się bez błędów!
        print(f"Wynik: {wynik}")
    finally:
        # finally wykonuje się zawsze
        print("Koniec programu!")
