def greatest_common_divisor(x, y):
    divisors = []
    if x > y:
        for divisor in range(1, x):
            if x % divisor == 0 and y % divisor == 0:
                divisors.append(divisor)
    if y > x:
        for divisor in range(1, y):
            if x % divisor == 0 and y % divisor == 0:
                divisors.append(divisor)

    return max(divisors)

print(greatest_common_divisor(32, 48))
