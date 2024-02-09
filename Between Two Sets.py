def getTotalX(a, b):
    a1 = 0
    for i in range(max(a), min(b)+1):
        if all(i % el == 0 for el in a) and all(el % i == 0 for el in b):
            a1 = a1 + 1
    return a1