from __future__ import annotations
from pathlib import Path
from typing import Any
import json

DATA_DIR = Path("data")
FILE_PATH = DATA_DIR / "filmy.json"

def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent=4)

def load_json(path: Path) -> Any:
    with path.open("r",encoding="utf-8") as f:
        return json.load(f)


def main():
    filmy = [
        {"title":"Nosferatu","year":2024,"genres":["horror",],"duration_min":142},
        {"title":"Incepcja","year":2010,"genres":["sci-fi","thriller"],"duration_min":156},
        {"title":"Zimna wojna","year":2018,"genres":["dramat","romans"],"duration_min":143},
        {"title":"Gladiator II","year":2024,"genres":["historyczny","dramat"],"duration_min":161},
    ]

    save_json(FILE_PATH, filmy)
    print(f"zapisano {len(filmy)} filmów do pliku {FILE_PATH}")

    wczytane = load_json(FILE_PATH)
    print(f"wczytano {len(filmy)} filmów z pliku {FILE_PATH}")

    po2012 = [f["title"] for f in wczytane if f.get("year", 0) >= 2012]
    print(f"filmy po roku 2012: {po2012}")


if __name__ == '__main__':
    main()
