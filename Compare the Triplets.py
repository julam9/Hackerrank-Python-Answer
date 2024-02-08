import os

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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
