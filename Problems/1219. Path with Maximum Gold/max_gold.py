class Solution:
    def getMaximumGold(self, grid):
        # set variables for the amount of rows and columns in the grid
        rows = len(grid)
        columns = len(grid[0])
        # set an empty variable to keep track of the max_gold found on a single path
        max_gold = 0

        # use recursion and depth first search algorithm
        def dfs(row, column):
            # check if the coordinates given are within the bounds of the grid
            # also check that the coordiante given does not contain 0 gold, if 0 gold return 0 and do not continue traversal
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] == 0:
                return 0
            
            # save current gold at coordinate to a variable
            curr = grid[row][column]
            # mark the current position as visited by setting its value to 0
            grid[row][column] = 0
            # start a sum of the gold found on a specific path
            local_max_gold = curr

            # use recursion to find the amount of gold that could be accumulated depending on possible next move
            left = dfs(row - 1, column)
            right = dfs(row + 1, column)
            top = dfs(row, column - 1)
            bottom = dfs(row, column + 1)

            # return the current grid position to its former value ( unmark it as visited )
            grid[row][column] = curr

            # set the local_max_gold found
            # curr plus the path that will yield the most gold
            local_max_gold = max(local_max_gold, curr + max(left, right, top, bottom))

            # return largest amount of gold possible to be found
            return local_max_gold
        

        # loop through the grid
        for row in range(rows):
            for column in range(columns):
                # if the value at the coordaintes is not 0 find the max amount of gold that can be obtained from staring at that point
                if grid[row][column] != 0:
                    # see if the amount of gold obtained is a new maximun
                    max_gold = max(max_gold, dfs(row, column))

        return max_gold