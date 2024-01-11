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

def calculate():
    number_list = []
    for number in range(100,1000):
        if is_palindrome(number):
            number_list.append(number)
    print(number_list)

calculate()