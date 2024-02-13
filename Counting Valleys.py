def countingValleys(steps, path):
    p2 = list(path)
    n_valley = 0
    for i in range(steps-1):
        while p2[i] == "D":
            i =+ 1
            continue
        else:
            n_valley += 1
            pass
    print(n_valley)
# testing
countingValleys(12, "DDUUDDUDUUUD")
#countingValleys(8, "UDDDUDUU")

