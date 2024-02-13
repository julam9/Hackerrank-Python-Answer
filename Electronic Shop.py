def getMoneySpent(keyboards, drives, b):
    prices_list = []
    for i in drives:
        for j in keyboards:
            prices_list.append(i+j)


# testing
getMoneySpent([2,3,4], [5,6,7], 20)