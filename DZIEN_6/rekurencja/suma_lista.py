def suma_lista(lista: list) -> int:
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

print(f"suma liczb: {suma_lista([1, 2, 3, 4, 5])}") 
