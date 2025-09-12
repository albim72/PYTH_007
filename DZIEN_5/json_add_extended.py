import json
from typing import Any, Dict

def add_to_json(file_path: str, new_data: Dict[str, Any]) -> None:
    """
    Dodaje nowe dane do pliku json tylko jeśli taki rekord jeszcze nie istnieje
    :param file_path:  ścieżka do pliku JSON
    :param new_data:  słownik z nowymi danymi do dodania
    :return:
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    if not isinstance(data, list):
        raise ValueError("Plik JSON nie zawiera listy jako głównej struktury")

    # zabezpieczenie przed duplikatami
    if new_data not in data:
        data.append(new_data)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        print(f"Rekord {new_data} już istnieje w pliku {file_path}")

if __name__ == '__main__':
    add_to_json('data/filmy.json', {
        'title': 'Misja',
        'year': 1986,
        'genres': ['dramat', 'historyczny'],
        'duration_min': 126
    })

    add_to_json('data/osoba.json', {"id": 1, "name": "Jan Kot", "city": "Kraków"})
    add_to_json('data/osoba.json', {"id": 2, "name": "Anna Król", "city": "Warszawa"})
    add_to_json('data/osoba.json', {"id": 2, "name": "Anna Król", "city": "Warszawa"})  # ten nie zostanie zapisany
