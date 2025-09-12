import json
from typing import Any, Dict

def add_to_json(file_path: str, new_data: Dict[str, Any]) -> None:
    """
    Dodaje nowe dane do pliku json
    :param file_path:  ścieżka do pliku JSON
    :param new_data:  słownik z nowymi danymi do dodania
    :return:
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    if isinstance(data, list):
        data.append(new_data)
    else:
        raise ValueError("Plik JSON nie zawiera listy jako głównej struktury")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    add_to_json('data/filmy.json', {'title': 'Misja', 'year': 1986, 'genres': ['dramat','hitoryczny'], 'duration_min': 126})
    add_to_json('data/osoba.json',{"id":1,"name":"Jan Kot","city":"Kraków"})
    add_to_json('data/osoba.json',{"id":2,"name":"Anna Król","city":"Warszawa"})
