def binary_to_int():
    with open('binary.txt', 'r') as file:
        data = file.read()
        data = data.split()
        finaldata = []
        print(data)
        for item in data:
            item = int(item, 2)
            finaldata.append(item)
        return finaldata


print(binary_to_int())