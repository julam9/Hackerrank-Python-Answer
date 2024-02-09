def plusMinus(arr):
    neg = 0 
    pos = 0 
    zero = 0 
    for x in arr: 
        if x < 0: neg += 1 
        elif x > 0: pos += 1 
        else: zero += 1 
        pos_ratio = pos/n 
        neg_ratio = neg/n 
        zero_ratio = zero/n 
    print('%.6f' % pos_ratio) 
    print('%.6f' % neg_ratio) 
    print('%.6f' % zero_ratio)