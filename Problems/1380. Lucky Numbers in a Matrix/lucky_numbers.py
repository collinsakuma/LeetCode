import math

class Solution:
    def luckyNumbers(self, matrix):
        output = [] # list to contain all lucky numbers in the matrix

        for i in range(len(matrix)): # loop though a range of the number of rows in the matrix
            # set row_min initial value to infinity
            # and a matching index to 0 to be replace by any new row_min
            row_min, index = math.inf, 0
            flag = True # set flag initialy to True

            # loop though range of the length of a row in the matrix
            for j in range(len(matrix[0])):
                # find the lowest value in the row, and set its value and index to row_min and index respectively
                if matrix[i][j] < row_min:
                    row_min, index = matrix[i][j], j
            
            # loop though range of # of rows in matrix
            for k in range(len(matrix)):
                # check the value of each row at index (index) to see if row_min is the greatest value in its column (index)
                if matrix[k][index] > row_min:
                    # if a value found is greater than row_min, then value row_min is not a lucky number set flag to False
                    flag = False
            
            if flag: # if flag still True then a lucky number has been found append that number to output list
                output.append(row_min)
        
        return output