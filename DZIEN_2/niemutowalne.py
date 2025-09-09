#krok 1 - zliczanie przefiltorwanych elementów
imiona = ["Anna","Alicja","Bartek","Andrzej","Karol","Agnieszka"]

wynik = len(
    list(
    map(lambda x: x.upper(),
        filter(lambda x: x.startswith("A"), imiona))
    )
)

print(f"funkcyjnie - liczba imion: {wynik}")
