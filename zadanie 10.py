def is_prime(x):
    divisors = []
    for number in range(1, x+1):
        if x % number == 0:
            divisors.append(number)
    
    #print(divisors)
    if len(divisors) == 2:
        return True
    else:
        return False
   
def calculate():
    liczby_pierwsze = []
    for i in range(1, 1000):
        if is_prime(i):
            liczby_pierwsze.append(i)
    return liczby_pierwsze[100-1]

print(calculate())
