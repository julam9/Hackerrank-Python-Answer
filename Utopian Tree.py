def utopianTree(n):
    tree_height=1
    if n==0: 
        tree_height = 1
    else :
        n1=1
        while n >= n1:
            if n1%2==0 : tree_height = tree_height + 1
            else : tree_height = tree_height * 2
            n1 += 1
    return tree_height    
    