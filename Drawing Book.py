def pageCount(n, p):
    startfrom_1 = p//2 
    if n%2 != 0:
        if n-p < 2:
            startfrom_n = 0
        else: 
            startfrom_n = p//2 + 1 
    else:
        if p < n:
            startfrom_n = p//2+1 
        else:
            startfrom_n = 0 
            
    return min(startfrom_1, startfrom_n)


# testing
pageCount(5,4)              
