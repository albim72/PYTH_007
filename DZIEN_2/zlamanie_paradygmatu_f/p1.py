def add_item(item, bag=[]):      # ← domyślna lista ŻYJE między wywołaniami
    bag.append(item)
    return bag

print(add_item("miecz"))         # ['miecz']
print(add_item("tarcza"))        # ['miecz', 'tarcza']  ← poprzedni stan wrócił z zaświatów
print(add_item("eliksir"))       # ['miecz', 'tarcza', 'eliksir']
