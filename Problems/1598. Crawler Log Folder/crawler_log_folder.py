class Solution:
    def minOperations(self, logs):
        output = 0 # keep track of what level of the files we are at
        for i in logs: # loop through all operations in logs
            if i[0] != ".": # check if the operation does not contain a "." meaning that it is an operation that navigates to a new subfolder
                output += 1 # increase depth of level by 1 of file structure
            elif ".." in i: # if operation is "../" to move to current folders parent folder
                if output: # first check if current level isnt main, if main you cannot move up anymore levels
                    output -= 1 # if output is not main level decrease level by 1
        return output # return however many levels deep last folder accessed is