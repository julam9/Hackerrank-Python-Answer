def pageCount(n, p):
    startfrom_1 = p//2  
    startfom_n = n//2 - p//2

    return min(startfrom_1, startfom_n)
# testing
pageCount(5,4)              
print(2//2)