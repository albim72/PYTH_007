#suma i średnia liczb - we: liczby rozdzielone spacjami

def main():
    text = input("Podaj liczby rozdzelone spacjami: ")
    numbers = list(map(int, text.split()))

    #obliczenia
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0

    #wynik

    print(f"suma: {total}")
    print(f"średnia: {avg:.2f}")

if __name__ == '__main__':
    main()
