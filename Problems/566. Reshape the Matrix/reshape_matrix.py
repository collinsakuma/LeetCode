class Solution:
    def matrixReshap(self, mat, r, c):
        all_num = [] # flatten all list in the list into one list of all the numbers
        new_mat = [] # create a list that will be given the appropriate number of rows and columns

        for row in mat: 
            for num in row:
                all_num.append(num) # turn all of the sub list into one long list of all numbers

        if r * c != len(all_num): # check if the row and column amounts is possible
            return mat # if the new row and column combination is not possible return the original mat( list )
        else:
            for row_index in range(r): # loop the number of times there are rows to create
                new_mat.append(all_num[row_index * c : row_index * c + c]) # for each row create a new list in the range of row_index * c (column) to index or row_index * c + c
            return new_mat # return the new list of list