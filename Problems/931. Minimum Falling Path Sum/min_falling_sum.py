import math

class Solution:
    def minFallingPathSum(self, matrix):
        length = len(matrix) # set a variable equal to th length of the matrix, matrix is n x n so no second height variable is needed

        pre = [0] * length # set the original dp

        # loop through the range of the rows in reverse order, loop from bottom of matrix to top
        for i in reversed(range(length)):
            # create a second dp with every element having infinity as its value
            cur = [math.inf] * length
            
            # second loop through the range of the length of the matrix, loop variables in each row
            for j in reversed(range(length)):
                # Check to see if index j has elements to the left of it
                if 0 <= j - 1:
                    # if it does set a to sum of previous row sum of index to the left
                    a = pre[j - 1]
                else: # if no element to the left of j set a to infinity
                    a = math.inf
                
                b = pre[j] # set b equal to the index directly under it

                if j + 1 < length: # if index j has element to its left
                    c = pre[j + 1] # set the sum of c to previous row and to the right of index
                else: # if no element to the right of index j set c to infinity
                    c = math.inf
                
                # set sum of cur[j] to the current element at row i index j plus the minimum value possible between a,b,c
                cur[j] = matrix[i][j] + min(a,b,c)

            pre = cur # after the entire row is solved set pre to the new values to represent the lowest possible sums before iterating the next row

        return min(pre)