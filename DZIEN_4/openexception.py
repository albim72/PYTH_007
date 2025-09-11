try:
    # próba otwarcia pliku do odczytu
    f = open("notatki.txt", "r", encoding="utf-8")
    print("Twoje dotychczasowe notatki:")
    zawartosc = f.read()
    print(zawartosc)
    f.close()
except FileNotFoundError:
    # drugą możliwością bardziej uniwersalną jest klasa Exception
    # jeśli pliku nie ma – tworzymy nowy
    print("Brak pliku notatki.txt – tworzę nowy dziennik.")
    f = open("notatki.txt", "w", encoding="utf-8")
    f.close()

# pytamy użytkownika o nową notatkę
nowa_notatka = input("Dodaj nową notatkę: ")

# zapisujemy notatkę na końcu pliku
f = open("notatki.txt", "a", encoding="utf-8")
f.write(nowa_notatka + "\n")
f.close()

print("Notatka została zapisana!")
