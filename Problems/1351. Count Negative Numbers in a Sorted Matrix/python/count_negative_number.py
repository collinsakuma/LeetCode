class Solution:
    def countNegative(self, grid):
        count = 0
        for arr in grid:
            for i in arr:
                if i < 0:
                    count += 1
        return count