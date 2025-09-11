from dataclasses import dataclass

#definicja zwykłej klasy
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name}, {self.price})"

#definicja klasy danych
@dataclass
class ProductData:
    name: str
    price: float


#utworzenie obiektów
product = Product("chleb", 4.56)
product_data = ProductData("mleko", 5.5)

print(product)
print(product_data)

