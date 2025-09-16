import json
from pathlib import Path

FILE = Path("people.json")

def load_data():
    """Ładuje dane z pliku JSON (lub pustą listę, jeśli plik nie istnieje)."""
    if FILE.exists():
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    """Zapisuje dane do pliku JSON."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_person(name, age):
    """Dodaje nową osobę do bazy."""
    data = load_data()
    data.append({"name": name, "age": age})
    save_data(data)

def show_people():
    """Wyświetla wszystkie osoby z pliku JSON."""
    data = load_data()
    if not data:
        print("Brak zapisanych osób.")
    else:
        print("\nLista osób:")
        for idx, person in enumerate(data, 1):
            print(f"{idx}. {person['name']} (wiek: {person['age']})")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Dodaj osobę")
        print("2. Pokaż osoby")
        print("3. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj imię: ")
            age = int(input("Podaj wiek: "))
            add_person(name, age)
            print("Osoba została dodana.")
        elif choice == "2":
            show_people()
        elif choice == "3":
            break
        else:
            print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
