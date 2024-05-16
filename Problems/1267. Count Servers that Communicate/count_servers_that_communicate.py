class Solution:
    def countServers(self, grid):
        rows, columns = len(grid), len(grid[0])
        points = []
        connections = 0

        row_connections = [0] * rows
        column_collections = [0] * columns

        # loop through the grid
        for row_i in range(rows):
            for column_i in range(columns):
                # if there is a server at the grid position
                # add a connections to the row and column that it is at
                if grid[row_i][column_i]:
                    row_connections[row_i] += 1
                    column_collections[column_i] += 1
                    # add a server point to the points array
                    points.append((row_i, column_i))

        # loop though points where there are servers
        for row_i, column_i in points:
            # check if there are other servers either on the same row and column as the current server
            # if there is another server in alignment increase connection count by 1
            if row_connections[row_i] > 1 or column_collections[column_i] > 1:
                connections += 1
        
        return connections