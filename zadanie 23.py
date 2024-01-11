def get_slices(word, slices):
    lista = []
    if slices < 1:
        raise ValueError('The length cannot be less than 1.')
    elif slices > len(word):
        raise ValueError('The length cannot be greater than sequence.')
    else:
        for i in range(len(word) - slices + 1):
            lista.append(word[i:i+slices])
        return lista


print(get_slices('esmartdata', 5))