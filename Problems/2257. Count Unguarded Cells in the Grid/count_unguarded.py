class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for wall in walls:
            grid[wall[0]][wall[1]] = 1

        def is_in(row, column):
            if row < 0 or row >= m or column < 0 or column >= n:
                return False
            else:
                return True

        def check_top(row, column):
            if is_in(row - 1, column):
                if grid[row - 1][column] != 1:
                    if grid[row - 1][column] == 2:
                        check_top(row - 1, column)
                    else:
                        grid[row-1][column] = 3
                        check_top(row-1, column)

        def check_right(row, column):
            if is_in(row, column + 1):
                if grid[row][column + 1] != 1:
                    if grid[row][column + 1] == 2:
                        check_right(row, column + 1)
                    else:
                        grid[row][column + 1] = 3
                        check_right(row, column + 1)
        
        def check_bottom(row, column):
            if is_in(row + 1, column):
                if grid[row + 1][column] != 1:
                    if grid[row + 1][column] == 2:
                        check_bottom(row + 1, column)
                    else:
                        grid[row + 1][column] = 3
                        check_bottom(row + 1, column)

        def check_left(row, column):
            if is_in(row, column - 1):
                if grid[row][column - 1] != 1:
                    if grid[row][column - 1] == 2:
                        check_left(row, column - 1)
                    else:
                        grid[row][column - 1] = 3
                        check_left(row, column - 1)


        for guard in guards:
            row, column = guard[0], guard[1]
            grid[row][column] = 2
            check_top(row, column)
            check_right(row, column)
            check_bottom(row, column)
            check_left(row, column)

        count = 0

        for i in grid:
            count += i.count(0)
        
        return count