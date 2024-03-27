import math

class Solution:
    def splitString(self, s):
        n = len(s)

        def recursive(index, parts, prev_val):
            # must be split into two or more parts if True than conditions have been met
            if index == n:
                return parts >= 2
            
            # loop in the range from the current index, to end of the list
            for i in range(index, n):
                # find the numeric value of the part from index to i plus 1
                num = int(s[index:i + 1])

                # if the prev_val is math.inf then this is the first part ( valid )
                # or if the prev_val - 1 equals the new part, if this condition is true then a new dereasing part has been found
                if prev_val == math.inf or num == prev_val - 1:
                    # recursively check the next indexes of the string for more stricktly decreasing parts by 1
                    if recursive(i + 1, parts + 1, num):
                        # if all recursive iterations pass, return true
                        return True
                    
            return False # return False as no decreasing pattern by 1 has been found
    
        # initalize the recursive solution
        return recursive(0, 0, math.inf)