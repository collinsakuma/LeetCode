class Solution:
    def restoreMatrix(self, rowSum, colSum):
        # set value for the number of rows and columms
        row, column = len(rowSum), len(colSum)
        # for the matrix grid of rows and columns
        grid = [[0 for _ in range(column)] for _ in range(row)]

        # loop through rows and columns
        for i in range(row):
            for j in range(column):
                # find the row and column sum 
                row_sum, column_sum = rowSum[i], colSum[j]
                # find the minimum value possible for that row and column 
                min_val = min(row_sum, column_sum)
                # set grid value to the minimum value possible
                grid[i][j] = min_val
                # reduce the row and column sum by the min value
                rowSum[i] -= min_val
                colSum[j] -= min_val

        return grid