class Solution:
    def convert(self, s, numRows):
        # if there is only one row then return s unchanged
        if numRows == 1:
            return s
        
        row_arr = [""] * numRows # 2D array that has the number of numRows in it
        row_idx = 1 # set initial row_idx to 1
        going_up = True # going_up with be a flag for if we are in the zig part of the list

        for ch in s: # loop through each character in s
            # add the character to list in row_arr, minus 1 to account for 0 index
            row_arr[row_idx - 1] += ch
            if row_idx == numRows: # when row_idx reaches numRows, we need to backtrack through row_arr, set going_up index to False
                going_up = False
            elif row_idx == 1: # when row_idx reaches starting point 1 reset it to True to continue to loop forward again
                going_up = True
            
            if going_up: # if still looping left to right in row_arr incresase row_idx by 1
                row_idx += 1
            else: # if looping right to left decrease row_idx by 1
                row_idx -= 1

        return "".join(row_arr) # join the row_arr into a string and return 