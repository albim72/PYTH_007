ksiazki = {
"978-83-240-0010-0":"Pan Tadeusz",
"978-83-240-0740-3":"Lalka",
"978-83-240-1256-3":"Quo Vadis",
}

print(ksiazki)
print(ksiazki["978-83-240-0010-0"])

ksiazki["978-83-240-2264-2"] = "Krzyżacy"
print(ksiazki)

#itercja po słowniku
print("______________ książki ______________")
for k,v in ksiazki.items():
    print(k,v)

#sprawdzenie kluczy
print("\nCzy mamy -> 978-83-240-2264-2??","978-83-240-2264-2" in ksiazki)
print("\nCzy mamy -> 978-83-240-2242-5??","978-83-240-2242-5" in ksiazki)
