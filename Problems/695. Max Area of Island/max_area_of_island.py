class Solution:
    def maxAreaOfIsland(self, grid):
        # variable for biggest island
        self.biggest_island = 0
        # variable for the size of the current island
        self.curr_area = 0

        # helper function to find the area of the island when it is found
        def is_land(x, y):
            # check if the coordinates are in bounds
            if x >= 0 and x <= (len(grid) - 1) and y >= 0 and y <= (len(grid[0]) - 1):
                # if the coordinate is land( part of an island )
                if grid[x][y] == 1:
                    grid[x][y] = 0 # mark that coordinate as visited
                    # increment the current area of the current island
                    self.curr_area += 1
                    # recursively check all of the positions around the coordinate
                    left = is_land(x - 1, y)
                    right = is_land(x + 1, y)
                    top = is_land(x, y - 1)
                    bottom = is_land(x, y + 1)

            else:
                None
            # check if a new bigggest island has been found
            self.biggest_island = max(self.biggest_island, self.curr_area)

        # loop through the rows and columns in the grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                # set the current island size to 0
                self.curr_area = 0
                # find the area of an island when found
                is_land(row, column)

        # return the biggegst island 
        return self.biggest_island