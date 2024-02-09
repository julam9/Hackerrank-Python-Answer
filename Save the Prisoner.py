def saveThePrisoner(n, m, s):
    #sweets left after first round
    sweets_left = m-(n-s+1)
    #if sweets left more than or equal to zero
    if sweets_left <= 0:
        warn_chair = s+m-1
    elif sweets_left % n == 0:
        warn_chair = n
    else : warn_chair = sweets_left%n
    return warn_chair
    