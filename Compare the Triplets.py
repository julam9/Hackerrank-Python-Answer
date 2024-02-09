def compareTriplets(a, b):
    p1=0
    p2=0
    for x,y in zip(a, b):
        if x>y :
            p1+=1
        elif y>x:
            p2+=1
        else:
            p1+=0
            p2+=0
    return [p1, p2]