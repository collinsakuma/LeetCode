class Solution:
    def matrixScore(self, grid):
        # get length of rows and columns
        rows, columns = len(grid), len(grid[0])

        # start with the most significant bits at the start all 1's
        res = (1 << (columns - 1)) * rows

        # loop through columsn and toggle the the column checking if it would increase the score or not
        for j in range(1, columns):
            val = 1 << (columns - 1 - j)
            set_count = 0

            for i in range(rows):
                if grid[i][j] == grid[i][0]:
                    set_count += 1

            res += max(set_count, rows - set_count) * val

        return res