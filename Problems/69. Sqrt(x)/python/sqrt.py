import math

class Solution:
    # first solution using build in function that are not supposed to be used.
    def mySqrtUsingBuiltInMethods(self, x):
        temp_answer = math.sqrt(x)
        if temp_answer != float:
            return int(temp_answer)
        else:
            split_float = temp_answer.split(".")
            return split_float[0]
    
    def mySqrt(self, x):
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            # compute mid 
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last