#własna funckja wyższego rzędu
def apply_twice(funkcja,value):
    return funkcja(funkcja(value))

#przykładowe funkcje
def dodaj_jeden(x):
    return x+1

def pomnoznie_2(x):
    return x*2

print(apply_twice(dodaj_jeden,5))
print(apply_twice(pomnoznie_2,5))
print(apply_twice(pomnoznie_2,-3.4))
print(apply_twice(pomnoznie_2,12.77))

print(apply_twice(lambda x: x+1,333.8))
print(apply_twice(lambda x: x*2,1.98))
