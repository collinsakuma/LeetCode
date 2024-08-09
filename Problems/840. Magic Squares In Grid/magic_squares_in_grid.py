class Solution:
    def numMagicSquaresInside(self, grid):
        rows, columns = len(grid), len(grid[0])
        magic_squares = 0

        if rows < 3 > columns: return 0

        # coordinates for the 3x3 square
        square_coordinates = {0: (-1, -1), 1: (-1, 0), 2: (-1, 1), 3: (0, -1), 4:(0, 0), 5: (0, 1), 6: (1, -1), 7: (1, 0), 8: (1, 1)}

        def is_magic_squares(row, column):
            # empty list to flatten the 3x3 matrix values
            nums_list = []

            # loop through range of coordinates to fill out flattened square
            for i in range(len(square_coordinates)):
                target = grid[row + square_coordinates[i][0]][column + square_coordinates[i][1]]
                # check if the number is not already present in the square and if the number is in range 1 - 9
                if target not in nums_list and 0 < target < 10:
                    nums_list.append(target)
                else:
                    return False
            
            # if all numbers in square are 1-9 check if rows, columns, and diagonals are all equal
            if check_rows(nums_list) and check_columns(nums_list) and check_diagonals(nums_list):
                return True
        
        # check if rows are all equal
        def check_rows(flattened_square):
            return sum(flattened_square[:3]) == sum(flattened_square[3:6]) == sum(flattened_square[6:])
        
        # check if columns are all equal
        def check_columns(flattened_square):
            return flattened_square[0] + flattened_square[3] + flattened_square[6] == flattened_square[1] + flattened_square[4] + flattened_square[7] == flattened_square[2] + flattened_square[5] + flattened_square[8]
        
        # check if diagonals are equal
        def check_diagonals(flattened_square):
            left = flattened_square[0] + flattened_square[4] + flattened_square[8]
            right = flattened_square[2] + flattened_square[4] + flattened_square[6]
            
            return left == right
        
        # loop through possible middle of square coordinates
        for row in range(1, rows - 1):
            for column in range(1, columns - 1):
                # the middle of the square can only be 5 skip checking if middle is not 5
                if grid[row][column] == 5:
                    # check if coordinate is the center of a magic square
                    if is_magic_squares(row, column):
                        magic_squares += 1
            
        # return count of magic squares
        return magic_squares