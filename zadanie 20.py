def hamming_distance(vector1, vector2):
    vector1 = list(vector1)
    vector2 = list(vector2)
    lenv1 = len(vector1)
    lenv2 = len(vector2)
    hamming_buff = 0

    if lenv1 != lenv2:
        raise ValueError('Both vectors must be the same length.')
    else:
        for i in range(0, lenv1):
            if vector1[i] != vector2[i]:
                hamming_buff = hamming_buff + 1
    
    return hamming_buff

print(hamming_distance('110', '10100'))