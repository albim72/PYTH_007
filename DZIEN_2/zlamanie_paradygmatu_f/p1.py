def add_item(item, bag=[]):      # ← domyślna lista ŻYJE między wywołaniami
    bag.append(item)
    return bag

print(add_item("miecz"))         # ['miecz']
print(add_item("tarcza"))        # ['miecz', 'tarcza']  ← poprzedni stan wrócił z zaświatów
print(add_item("eliksir"))       # ['miecz', 'tarcza', 'eliksir']

print(add_item("miecz"))
print(add_item("proca"))

#rozwiązanie bezpieczne
def add_item_safe(item, bag=None):
    bag = [] if bag is None else list(bag)
    bag.append(item)
    return bag

print(add_item_safe("miecz"))         # ['miecz']
print(add_item_safe("tarcza"))        # ['miecz', 'tarcza']  ← poprzedni stan wrócił z zaświatów
print(add_item_safe("eliksir"))
