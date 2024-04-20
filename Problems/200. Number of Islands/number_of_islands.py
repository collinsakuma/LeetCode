class Solution:
    def numIslands(self, grid):
        # set variables for number of rows and columns
        rows = len(grid)
        columns = len(grid[0])
        num_islands = 0

        def dfs(row, column):
            # if grid position is outside of grid bounds return None
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] != '1':
                return None
            # mark grid position once traveled too
            grid[row][column] = '0'

            # check surrounding grid positions if they are part of the island and mark those parts are visited ('0')
            dfs(row + 1, column)
            dfs(row - 1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)

        # loop though grid
        for row in rows:
            for column in columns:
                # if island is found count the island
                if grid[row][column] == '1':
                    num_islands += 1
                    # recursively check surrounding grid positions for if they are part of the island 
                    dfs(row, column)
        
        return num_islands