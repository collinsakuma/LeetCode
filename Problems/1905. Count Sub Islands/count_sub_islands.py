class Solution:
    def countSubIslands(self, grid1, grid2):
        # count of sub islands
        sub_islands = 0
        # number of rows and columns
        rows, columns = len(grid1), len(grid1[0])

        # directions for verticle and horizional coordinates
        directions = {0:(0, -1), 1:(-1,0), 2:(0,1), 3:(1,0)}

        # recursive DFS search to find islands
        def find_islands(row, column):
            # check if the coordinate is out or bounds or if the coordinate is not land
            if row < 0 or row >=rows or column < 0 or column >= columns or grid2[row][column] == 0:
                # return if conditions fail
                return
            # mark that land has been traversed
            grid2[row][column] = 0
            # loop through the possible direction of neighboring coordinates
            for i in range(4):
                # recursively check the surrounding coordinates
                find_islands(row + directions[i][0], column + directions[i][1])

        # remove non common sub islands
        for row in range(rows):
            for column in range(columns):
                # if grid position is not land on grid1 but island on grid2 remove the non common land
                if grid1[row][column] == 0 and grid2[row][column] == 1:
                    find_islands(row, column)

        # count the sub islands
        for row in range(rows):
            for column in range(columns):
                if grid2[row][column] == 1:
                    find_islands(row, column)
                    sub_islands += 1

        return sub_islands