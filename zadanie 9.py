def is_prime(x):
    divisors = []
    for number in range(1, x+1):
        if x % number == 0:
            divisors.append(number)
    
    print(divisors)
    if len(divisors) == 2:
        return True
    else:
        return False

