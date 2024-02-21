class Solution:
    def rangeBitwiseAnd(self, left, right):
        shift = 0

        # while left and right limits are not equal
        while left < right:
            # right shift the left limit by 1 bit
            left >>= 1
            # right shift the right limit by 1 bit
            right >>= 1
            # increment shift variable by 1
            shift += 1
        
        # left shift the left limit by shift and return the results
        return left << right