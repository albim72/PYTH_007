print("Witaj w świecie Pythona!")
x:int = 5.99
y:float = 7
print(x+y)
print(type(x))
print(type(y))

x = "jedynka" #zniszzenie zmiennej x z linii 2 i utworzenie nowej w typie str
print(x)
print(type(x))

def multiply(a,b):
    return a*b

print(multiply(5,6))
print(multiply(-2,9.3))

n = 9
k =15
print(multiply(n,k))

_r_ = 0.0045 #zmienna typu protected - chroniona
print(_r_)
print(type(_r_))

__info = "ważna informacja" #zmienna typu private
print(__info)
print(type(__info))

#nazwy zabronione: __init__, __str__, __new__, i ponad 200 innych -> funkcje specjalne, magiczne, dunder functions

#! NIE RÓB TEGO
# __init__ = "blokujemy...."
# print(__init__)
# print(type(__init__))

u = "12.75"
print(u*9)

# print(int(u)*9)
print(eval(u)*9)
