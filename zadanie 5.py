def calculate(x):
    lista = []
    dzielnik = 2
    while x != 1:
        if (x % dzielnik) == 0:
            lista.append(dzielnik)
            x = x / dzielnik
        else:
            dzielnik += 1
    return lista[len(lista)-1]

print(calculate(13195))