funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])   # [2, 2, 2]  ← wszystkie patrzą na TEGO SAMEGO i (ostatnią wartość)
