class Solution:
    def countNegative(self, grid):
        count = 0
        for arr in grid:
            for i in arr:
                if i < 0:
                    count += 1
        return count

    # second solution with 0(n + m) complexity
    def CountNegativeSolutionTwo(self, grid):
        n = len(grid[0])  # find the length of the arrays in the array (aka the columns)
        row = len(grid) - 1 # find how many rows there are in the grid
        column = 0 # set the initial column value for iteration
        negative_count = 0 # set the starting count of negative numbers
        while row >= 0 and column < n:
            if grid[row][column] < 0:
                negative_count += n - column
                # because numbers are arranged in non-increasing order(decreasing) if the first number encountered
                # is negative the remaining numbers in that row must also be negative hence (n - column)
                # if the row = [-1,-1,-2,-3] then grid[row][0] < 0 meaning all numbers after are also negative
                # so negative_count is increased by n(length of the row) - 0(the first index) adding 4 to the count.
                row -= 1
                # if negative number is found then that row does not need to be looped through anymore so is decreased by 1 
                # it is decreased because the function loops through in reverse row order.
            else:
                column += 1
                # - if the number at grid[row][column] is not less than 0 meaning the number is positive the column value is 
                #   incremented by 1. 
                # - Example: 
                #   - if grid[0](row 1) = [3,2,1,-1]
                #   - if the index position being checked is grid[0][0] (grid [row[0]][column[0]) 
                #   - it will return false because 3 is greter than 0 incrementing the column value by 1
                #   - the next loop with look at grid[0][1] or 2.
        return negative_count