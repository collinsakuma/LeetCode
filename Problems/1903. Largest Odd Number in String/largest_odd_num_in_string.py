class Solution:

    # first solution exceeds linigt for integer string conversion otherwise words except for super large numbers over 4300 characters
    def largestOddNumber(self, num):
        n = len(num)

        while n != 0: # while n does not equal 0 continue loop
            if int(num[:n]) % 2 != 0: # first loop will take entire num while each loop will remove the last number off num 
                return (num[:n])
            n -= 1 # reduce n by 1 next loop will loop at len(num) - 1
        return ""
    
    