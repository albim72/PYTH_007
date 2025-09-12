from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    name: str
    price: float
    quantity: int


class ShoppingList:
    def __init__(self) -> None:
        self.items: List[Item] = []

    def add_item(self,item: Item) -> None:
        self.items.append(item)

    def total_cost(self) -> float:
        return sum(i.quantity * i.price for i in self.items)

    def export_txt(self,path:str) -> None:
        with open(path,"w",encoding="utf-8") as f:
            for i in self.items:
                f.write(f"{i.name} | ilość: {i.quantity} | cena: {i.price:.2f} zł"
                        f" | kwota za produkt: {i.quantity * i.price:.2f} zł\n")

def main() -> None:
    shopping = ShoppingList()

    #produkty
    shopping.add_item(Item("chleb",4.2,2))
    shopping.add_item(Item("mleko",3.88,3))
    shopping.add_item(Item("twaróg",7.8,4))
    shopping.add_item(Item("kabanosy",9.99,2))
    shopping.add_item(Item("łosoś",12.8,2))

    #zapis do pliki
    shopping.export_txt("shopping.txt")

    #wydruk na konsoli
    print(f"suma zakupów: {shopping.total_cost():.2f} zł")

if __name__ == '__main__':
    main()
