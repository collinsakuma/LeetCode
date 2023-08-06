class Solution:
    def diagonalSum(self, mat):
        output = 0 # variable to keep track of sum
        n = len(mat) 
        mid = n // 2 # mid index of mat

        for i in range(n): # loop though range of len(n)
            output += mat[i][i] # for diagonal top left to bottom right 
            output += mat[n - 1 - i][i] # fro diagonal from top right to bottom left

        if n % 2 == 1: # if mats length is an odd number that means that the number at the middle has been added twice so we need to reduce output by its value once
            output -= mat[mid][mid] # value at mat[mid][mid] is the value at the middle of the matrix
        
        return output # return the output