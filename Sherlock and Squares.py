import math

def squares(a, b): 
    result = 1 if a**(1/2)%1==0 else 0
    lowb = int(a**(1/2)) if a**(1/2)%1==0 else int(math.floor(a**(1/2)))
    uppb = int(b**(1/2)) if b**(1/2)%1==0 else int(math.floor(b**(1/2)))
    result = result + uppb - lowb
    return result