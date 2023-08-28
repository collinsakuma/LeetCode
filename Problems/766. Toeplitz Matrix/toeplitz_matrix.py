class Solution:
    def isToeplitzMatrix(self, matrix):
        for i in range(1, len(matrix)): # loop though range of 1 to len(matrix) this will loop through each row
            for j in range(1, len(matrix[0])): # second loop through range 1 to len(matrix[0]) this will loop through each column in the row
                if matrix[i-1][j-1] != matrix[i][j]: # check if each element is equal to the element to the top left of it so check [0][0] for element [1][1]
                    return False
        return True