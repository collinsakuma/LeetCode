class Solution:
    def generate(self, numRows):
        output = [] # set empty list to hold list of rows
        output.append([1]) # set initial row for output, top of triangle
        for i in range(numRows - 1): # loop though a range of numRows - 1, minus 1 for 0 index
            newRow = [1] # new rows first number will always be 1
            for j in range(i): # loop though range of what row is being generated
                newRow.append(output[i][j] + output[i][j + 1]) # generate new row by adding values from the previous row
            newRow.append(1) # all rows numbers end in 1 as well
            output.append(newRow) # append the new row to the output

        return output