#silnia n! = 1*2*...*n, n>=0, n należy do C(nieujmenych)

def silnia(n:int) -> int:
    if n == 0 or n == 1: #warunek zatrzymania - base case
        return 1
    return n * silnia(n-1)

print(silnia(5))
k = silnia(500) #!niewairygodne.... double n! dla n=171 daje błąd przekroczenia typu
print(k)
print(type(k))
