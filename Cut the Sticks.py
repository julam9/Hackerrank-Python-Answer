def cutTheSticks(arr):
    sticks_cut = []
    while len(arr) > 0:
        sticks_cut.append(len(arr))
        arr = [el for el in arr if el != min(arr)]
        arr = [el-min(arr) for el in arr]
    return sticks_cut        
        