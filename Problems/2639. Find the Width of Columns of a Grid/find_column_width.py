class Solution:
    def findColumnWidth(self, grid):
        # create an empty list of a length of the same number of columns to 
        # hold the max length in the column
        widths = [0] * len(grid[0])

        # loop through the columns
        for column in grid:
            # loop through the widths of the column
            for i in range(len(grid[0])):
                # find the length of the integer
                # - abs() to convert a negative number to positive
                # - str() to convert the number to a string
                # - len() to find the length of the integers
                width = len(str(abs(column[i])))
                # if the original number was negative increment its witdh
                # by 1 to account for the '-' sign
                if column[i] < 0:
                    width += 1
                
                # check if it is the greatest width for that column
                widths[i] = max(widths[i], width)

        return widths