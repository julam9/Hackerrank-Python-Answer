def findDigits(n):
    n_divider=0
    for digit in str(n):
        if int(digit)==0:
            pass
        elif int(n)%int(digit)==0:
            n_divider+=1
        else: n_divider+=0
    return n_divider