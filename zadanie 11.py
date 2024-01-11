def is_palindrome(number):
    x = number
    number = list(str(number))
    #print(number)
    if number == number[::-1]:
        bin_number = bin(x)
        bin_number = bin_number[2:]
        bin_number = list(str(bin_number))
        #print(bin_number)
        #print(bin_number[::-1])
        if bin_number == bin_number[::-1]:
            return True
        else:
            return False 
    else:
        return False

print(is_palindrome(99))