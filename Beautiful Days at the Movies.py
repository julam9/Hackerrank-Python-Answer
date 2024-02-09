def beautifulDays(i, j, k):
    beautifulday=[days for days in range(i,j+1) if abs(days-int(str(days)[::-1]))%k==0]
    return len(beautifulday)
        