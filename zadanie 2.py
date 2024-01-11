def calculate():
    lista = []
    for liczba in range(100):
        if (liczba % 5) == 0 or (liczba % 7) == 0:
            lista.append(liczba)
    print(sum(lista))
        
calculate()