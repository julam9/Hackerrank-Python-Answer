def kangaroo(x1, v1, x2, v2):
    answer = 'p'
    if x1<x2 and v1>v2:
        diff=v1-v2
        dist=x2-x1
        answer = 'YES' if dist%diff==0 else 'NO'
    elif x1>x2 and v1<v2:
        diff=v2-v1
        dist=x1-x2
        answer = 'YES' if dist%diff==0 else 'NO'    
    elif (x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (x1==x2 and v1!=v2) or (x1!=x2 and v1==v2): answer = 'NO'
    else: answer='YES' 
    return answer