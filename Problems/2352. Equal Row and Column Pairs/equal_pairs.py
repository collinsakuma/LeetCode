from collections import defaultdict

class Solution:
    def equalPairs(self, grid):
        count = 0 # set count variable to track count of equal row and column pairs
        m = defaultdict(int) # create a dictionary that will story frequency of rows in the grid key is a string version of the row with a number value

        # iterate over each row adding a new dict entry to m with a value of how many times that same row exist
        for row in grid:
            m[str(row)] += 1

        for i in range(len(grid[0])): # loop though range of the first row
            col = [] # set empty column list for each loop 
            for j in range(len(grid)): # second loop to get the different column values for the rows
                col.append(grid[j][i]) # append each element in a given column i 
            count += m[str(col)] # check many many time col appears in the dictionary m and add that frequency to count
        return count