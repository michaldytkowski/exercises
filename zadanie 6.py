def calculate():
    i = 0
    for number in range(100,1000):
        number = list(str(number))
        if number[0] == number[2]:
            #print(number)
            i = i + 1
    print(i)

calculate()