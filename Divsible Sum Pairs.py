def divisibleSumPairs(n, k, ar):
    n2=0
    for i in range(0, n):
        for j in range(0, n):
            if i<j and (ar[i]+ar[j])%k==0:
                n2=n2+1
    return n2