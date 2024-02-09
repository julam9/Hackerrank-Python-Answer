import math

def viralAdvertising(n):
    liked=0
    shared=5
    liked=liked+math.floor(shared/2)
    for days in range(1, n):
        shared=math.floor(shared/2)*3
        liked=liked+math.floor(shared/2)
    return liked