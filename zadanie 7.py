def calculate():
    wyniki = []
    for i in range(10,100):
        for j in range(10,100):
            wynik = j * i
            wynik2 = list(str(wynik))
            #print(wynik)
            if wynik2[0] == wynik2[len(wynik2) - 1]:
                wyniki.append(wynik)
            
    #print(wyniki)
    return wyniki[len(wyniki) - 1]

print(calculate())