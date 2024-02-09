def birthday(s, d, m):
    n_ways = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            n_ways = n_ways + 1
    return n_ways