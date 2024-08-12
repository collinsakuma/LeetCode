from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        # all possible directions that the next move can be
        directions = [(-1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1),  (1, -1)]

        # if starting position is not a 0 then return -1
        if grid[0][0] == 1:
            return -1
        
        # initalize a que with the starting location being at 0,0 with a visited length of 1
        q = deque([[0,0,1]])

        # while there are still coordinates in the que continue the loop
        while len(q) > 0:
            # pop the first coordaintes and length from the que
            row, column, length = q.popleft()

            # if the coordinates are the finishing point (bottom left corner of matrix) return the length
            if row == column == n - 1:
                return length
            
            # loop through the possible mov directions
            for x, y in directions:
                c_row, c_column = row + x, column + y

                # check if the directions are possible (in bound) and if the value at position is 0
                if 0 <= c_row < n and 0 <= c_column < n and grid[c_row][c_column] == 0:
                    # if so mark the coordinate as visited 
                    grid[c_row][c_column] = 1
                    # add the coordainte and new length to the que
                    q.append([c_row, c_column, length + 1])
        
        return -1 # if no possible moves can be made and we havent reached the target coordainte return -1