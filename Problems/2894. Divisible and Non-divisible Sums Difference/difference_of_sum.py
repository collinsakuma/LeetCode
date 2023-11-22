class Solution:
    def differenceOfSums(self, n, m):
        num_1, num_2 = [], [] # two arrays to track numbers
        for i in range(1, n + 1): # loop through range of n 
            if i % m != 0: # if i is not divisible by m append i to num_1 list
                num_1.append(i)
            else:
                num_2.append(i) # if i is divisible by m append i to num_2 list
        return sum(num_1) - sum(num_2)
    