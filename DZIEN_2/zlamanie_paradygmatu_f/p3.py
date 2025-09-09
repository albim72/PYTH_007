# więzione cienie  - pożne wiązanie w lambdach
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])   # [2, 2, 2]  ← wszystkie patrzą na TEGO SAMEGO i (ostatnią wartość)

#jak bezzpieczniej!
funcs_fix = [lambda i=i: i for i in range(3)]
print([f() for f in funcs_fix])
