from abc import ABC, abstractmethod
from pathlib import Path

#klasyczny interface
class Storage(ABC):
    @abstractmethod
    def save(self, path: Path, data: bytes) -> None: ...
    @abstractmethod
    def load(self, path: Path) -> bytes: ...


class FileStorage(Storage):
    def save(self, path: Path, data: bytes) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def load(self, path: Path) -> bytes:
        return path.read_bytes()

def client_code(storage: Storage) -> None:
    test_path = Path("test.txt")
    storage.save(test_path, b"test do zapisu")
    data = storage.load(test_path)
    print(f"Odczytano {data.decode('utf-8')!r} z {test_path.absolute()}")

client_code(FileStorage())

