class Solution:
    def oddsCells(self, m, n, indices):
        # create the 2D matrix with m as rows and n as columns
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        odds = 0 # count of odd numbers in the matrix

        for op in indices: # loop through the indicies
            # set the row and columns to be incremented
            r, c = op[0], op[1]
            
            for i in range(n): # loop though a range of the length of rows
                matrix[r][i] += 1 # increment the entire row of r
            
            for j in range(m): # loop though a range of the number of columns
                matrix[j][c] += 1 # increment all values in column c

        matrix = [element for row in matrix for element in row] # flatten the matrix into a single list

        for num in matrix: # count the number of odd numbers in the list
            if num % 2 != 0:
                odds += 1

        return odds