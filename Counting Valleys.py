def countingValleys(steps, path):
    p2 = list(path)
    n_valley = 0
    if p2[steps-1] == "U":
       for i in range(steps):
           if p2[i] == p2[i-1]:
               n_valley =+ 1
           else:
               continue
    else:
        n_valley= 0

    print(n_valley)

# testing
countingValleys(8, "UDDDUDUU")

