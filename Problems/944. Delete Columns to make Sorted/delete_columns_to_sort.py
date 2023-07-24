class Solution:
    def minDeletionSize(self, strs):
        columns = 0 # variable to keep track of columns that need to be deleted

        for i in range(len(strs[0])): # loop though range of the length of the first string
            for j in range(1, len(strs)): # start a second loop from 1 to the number of rows there are
                if strs[j][i] < strs[j - 1][i]: # compare the row to the one that comes before it and see if the letter is before the one at the same index of the previous row
                    # strs[1][0] < strs[0][0] will be the first letter checked if at those indexes are a and b it will evaluate as true and add 1 to the columns count
                    columns += 1
                    break # if statement evaluates to true this loop can be exited because they column needs to be removed and the rest of it doesnt need to be checked
        return columns