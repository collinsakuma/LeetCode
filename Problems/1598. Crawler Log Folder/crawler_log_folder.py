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
    
    def minOperationsTwo(self, logs):
        depth = 0 # track the current depth of file
        
        # loop through operations
        for operation in logs:
            # if ../ operation to return to parent folder
            if '..' in operation:
                # if depth is already at the root level do nothing as there are no higher folder
                if depth == 0:
                    continue
                # move up a folder and reduce the depth by 1
                else:
                    depth -= 1
            # ./ stay in current file
            elif '.' in operation:
                continue
            # move to a folder in the current folder, increase the depth level
            else:
                depth += 1
        
        return depth