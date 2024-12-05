class Solution:
    def canChange(self, start, target):
        # if the strings do not match after all of the strings have been removed, return false
        # as they cannot be moved to match
        if start.replace('_','') != target.replace('_',''):
            return False
        
        # set two pointers
        i = j = 0
        n = len(start)

        # loop through the indexes of the two strings
        while i < n and j < n:
            # while spaces continue the loop
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            # - if the letter reached in start is an L and its index is less than j currently 
            #   it cannot be moved right to match target string (Return False)
            # - if the letter reached in start is an R and its index is greater than j currently
            #   it cannot be moved left to match target (Return False)
            if i < n and j < n and (start[i] == 'L' and i < j or start[i] == 'R' and i > j):
                return False
            # increment both indexes
            i += 1
            j += 1
        return True