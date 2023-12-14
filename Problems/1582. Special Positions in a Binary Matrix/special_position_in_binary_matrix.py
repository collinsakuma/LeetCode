class Solution:
    def numSpecial(self, mat):
        count = 0 # keep count of special positions
        m = len(mat) # number of rows
        n = len(mat[0]) # number of columns

        for row in range(m): # loop though range of rows
            for col in range(n): # loop though range of columns
                if mat[row][col] == 0: # check if the current position is 0
                    continue # if position 0 countinue the loop of columns

                good = True # set flag to True

                for r in range(m): # loop though range of rows
                    if r != row and mat[r][col] == 1: # check if r is not the current row being looped and position is equal to 1
                        good = False # set flag to false ( meaning there is already a 1 in this row)
                        break # break from loop

                for c in range(n): # loop though range of columns
                    if c != col and mat[row][c] == 1: # if c is a different column that current col being looped and there is a 1 in the current column
                        good = False # set flag to false ( a 1 has been found in the same column)
                        break

                if good: # if flag is good, increase count of special numbers by 1
                    count += 1

        return count