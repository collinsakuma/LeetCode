class Solution:
    def largestLocal(self, grid):
        n = len(grid) - 2
        matrix = []


        # loop through matrix
        for i in range(n):
            matrix_row = []
            for j in range(n):
                # create a flattened list of all the values in the possible 3x3 grid area
                flattened_grid = []
                flattened_grid.append(grid[i][j])
                flattened_grid.append(grid[i][j+1])
                flattened_grid.append(grid[i][j+2])
                flattened_grid.append(grid[i+1][j])
                flattened_grid.append(grid[i+1][j+1])
                flattened_grid.append(grid[i+1][j+2])
                flattened_grid.append(grid[i+2][j])
                flattened_grid.append(grid[i+2][j+1])
                flattened_grid.append(grid[i+2][j+2])
                # append the largest value to the matrix row
                matrix_row.append(max(flattened_grid))
            # add the matrix row to the matrix
            matrix.append(matrix_row)
        
        return matrix # return thte matrix