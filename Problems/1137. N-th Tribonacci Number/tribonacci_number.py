class Solution:
    def tribonacci(self, n):
        # create a list of length 38 # set the first 3 positions
        f_array = [0] * 38
        f_array[1] = 1
        f_array[2] = 1

        # loop through a range of n, skipping the first three positions becuase their values are set
        for i in range(3, n + 1):
            # set index i value in loop 
            f_array[i] = f_array[i - 1] + f_array[i - 2] + f_array[i - 3]
        
        return f_array[n] # return value at index n
    