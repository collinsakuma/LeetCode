from collections import defaultdict

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
    
    def countUnguardedTwo(self, m, n, guards, walls):
        grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        wall = defaultdict(int)

        # Mark walls and guards in the grid
        for x, y in walls: 
            wall[(x, y)] = 1
            grid[x][y] = 2  # Mark walls
        for x, y in guards:
            grid[x][y] = 3  # Mark guards

        # DFS to mark guarded cells in a specific direction
        def dfs(row, column, direction):
            r, c = row + direction[0], column + direction[1]
            while 0 <= r < m and 0 <= c < n:
                if wall[(r, c)] == 1 or grid[r][c] == 3:  # Stop if encountering a wall or another guard
                    break
                grid[r][c] = 1  # Mark as guarded
                r, c = r + direction[0], c + direction[1]

        # Process guards
        for guard in guards:
            for i in range(4):  # Check all four directions
                dfs(guard[0], guard[1], directions[i])

        # Count unguarded cells
        unguarded_count = sum(1 for row in range(m) for col in range(n) if grid[row][col] == 0)

        return unguarded_count