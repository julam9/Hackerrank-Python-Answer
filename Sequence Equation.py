def permutationEquation(p):
    modified_p = [0] + p
    y=[]
    for x in range(len(p)):
       y.append(modified_p.index(modified_p.index(x+1)))
    return y  