class Solution:

    # first solution RUNTIME ERROR, exceeds integer string conversion limits
    def maxValue(self, n, x):
        # check if n is a negative number
        if n[0] != '-':
            # loop though range of length n
            for i in range(len(n)):
                # if x is greater than current n[i] value then x should be insterted before index i
                if int(n[i]) < x:
                    # combine the string with x before index i
                    return n[:i] + str(x) + n[:i]
            # if no number is less than x add x to the end of the string n
            return n + str(x)
        
        # if number  is a negative number 
        else:
            # loop though range of length n starting at index 1 because index 0 is "-"
            for j in range(1, len(n)):
                # if the current value at index j is greater than x, x should be inserted before j
                if int(n[j]) > x:
                    # combine the string with x before index j
                    return n[:j] + str(x) + n[j:]
            return n + str(x)
        
    def maxValueTwo(self, n, x):
        if n[0] == '-': # if n is negative 
            i = 1 # set i to 1 as index 0 is '-'
            # while i is less than length of n and current value at index i is less than of equal to x
            while i < len(n) and int(n[i]) <= x:
                # increment i by 1
                i += 1
            
        else:
            # set i equal to 0
            i = 0
            # loop while i is less than length n and value at index i is greater than or equal to x
            while i < len(n) and int(n[i]) >= x:
                # increment i by 1
                i += 1

        return n[:i] + str(x) + n[i:]