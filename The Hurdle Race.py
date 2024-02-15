class Solution:
    def hurdleRace(k, height):
        if k <= max(height):
            return max(height) - k 
        else:
            return 0 

# testing 
k=1
h=[1, 6, 3, 5, 2]

Solution.hurdleRace(k,h)
