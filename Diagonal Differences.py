import os

def diagonalDifference(arr):
    diag1, diag2 = sum([arr[i][i] for i in range(n)]), sum([arr[j-1][-j]for j in range(1,n+1)])    
    return abs(diag1-diag2)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()