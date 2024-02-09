def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_fall = [a + apple for apple in apples]
    orange_fall = [b + orange for orange in oranges]
    n_apple = [a1 for a1 in apple_fall if a1 in range(s,t+1)]
    n_orange = [o1 for o1 in orange_fall if o1 in range(s,t+1)]
    print(len(n_apple))
    print(len(n_orange))