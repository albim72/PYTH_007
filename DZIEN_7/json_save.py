import json

def main():
    data = {"name": "Anna", "age": 25}

    # zapis do pliku JSON
    with open("person.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # odczyt z pliku JSON
    with open("person.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("Dane odczytane z pliku JSON:")
    print(loaded)

if __name__ == "__main__":
    main()
