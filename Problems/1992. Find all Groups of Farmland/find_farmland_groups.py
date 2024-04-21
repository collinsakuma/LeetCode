class Solution:
    def findFarmLand(self, land):
        rows = len(land)
        columns = len(land[0])
        coordinates = []

        def dfs(row, column):
            # if not in grid return 0, 0
            if row < 0 or row >= rows or column < 0 or column >= columns or land[row][column] == 0:
                return (0, 0)
            # mark grid position as visited
            land[row][column] = 0

            # farm land aer stritly in squares so ony need to traverse the the right and bellow
            row_1, col_1 = dfs(row + 1, column)
            row_2, col_2 = dfs(row, column + 1)

            # find the bottom right coordinate of the farmland
            farm_row = max(row_1, row_2, row)
            farm_column = max(col_1, col_2, column)

            # return bottom right farmland coordinate
            return (farm_row, farm_column)
        
        # loop through 2D matrix
        for row in range(rows):
            for column in range(columns):
                # if a parcel of land is found find its bottom right point
                if land[row][column] == 1:
                    # set x, y to the bottom right coordinate of the farmland
                    x, y = dfs(row, column)
                    # append the whole coordinates of the found farmland parcel
                    coordinates.append([row, column, x, y])

        return coordinates