expr = "__import__('os').system('echo PWNED > pwned.txt')"
print(eval(expr))

#naiwne sandboxowanie
# user_expr = "print(4+6)"
user_expr = "().__class__.__base__.__subclasses__()"
#próba zabezpieczenia środowiska
res= eval(user_expr,{"__builtins__":None},{})

