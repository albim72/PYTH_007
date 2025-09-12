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
                        f" | {self.total_cost():.2f} zł\n")
