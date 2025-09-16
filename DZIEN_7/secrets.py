import random
token = ''.join(random.choice('abcd') for _ in range(20)) #kryptograficznie niebezpieczny

print(token)

import secrets

tokens = secrets.token_hex(20) #kryptograficznie bezpieczny
print(tokens)
