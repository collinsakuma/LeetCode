class Solution:
    def islandPerimeter(self, grid):
        # set variables for column and row amount
        columns = len(grid[0])
        rows = len(grid)
        perimeter = 0

        # loop though range of rows and columns
        for row in range(rows):
            for column in range(columns):
                # if the grid space is part of the island
                if grid[row][column] == 1:
                    # increase the perimeter by 4 for all four sides
                    perimeter += 4
                    # if the row is not the top row check if the grid space above is also part of the island
                    if row > 0 and grid[row - 1][column] == 1:
                        # if space above is also part of the island reduce perimeter by 2 for the sides lost from the intersection
                        perimeter -= 2
                    # if the column is not the first column check if the grid space to the right is also part of the island
                    if column > 0 and grid[row][column - 1] == 1:
                        # if grid place to the left is part of the island reduce perimeter total for intersecting sides
                        perimeter -= 2
        
        return perimeter
    

    #### Second Solution using DFS / Recursion ####
    def islandPerimeterTwo(self, grid):
        columns = len(grid[0])
        rows = len(grid)
        perimeter = 0

        def dfs(row, column):
            # check if the adjacent sides are valid grid locations
            # if not valid locations then a side is garunteed to be there as no intersection land can bee in that position
            if row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] == 0:
                # return that there is a vaid side
                return 1
            # if the gid position equals -1 that this is an already accounted for gird spot, return 0
            if grid[row][column] == -1:
                return 0
            # mark the current grid spot as already visited
            grid[row][column] = -1
            
            # check the 4 adjacent sides 
            return (dfs(row + 1, column) +
                    dfs(row - 1, column) +
                    dfs(row, column + 1) +
                    dfs(row, column - 1))
        
        # loop though grid positions
        for row in range(rows):
            for column in range(columns):
                # if the grid position is valid, run the dfs() function to check its adjacent positions
                if grid[row][column] == 1:
                    # add the number of valid sides that is returned
                    perimeter += dfs(row, column)

        return perimeter