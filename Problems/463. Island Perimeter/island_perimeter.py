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