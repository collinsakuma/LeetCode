class Solution:
    def checkXMatrix(Self, grid):
        n = len(grid)

        for i in range(n): # loop though all of the rows
            for j in range(n): # loop though each element in each row
                if j == i or j == n - i - n: # check pattern from top left to bottom left
                    if grid[i][j] == 0:
                        return False
                else: 
                    if grid[i][j] != 0:
                        return False
        return True