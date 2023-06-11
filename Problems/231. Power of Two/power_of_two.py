class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0: # if n is less 0 is cannot be a power of 2
            return False
        if n == 1: # 1 is a special case because 2 ** 0 is 1 return True
            return True
        while n % 2 == 0:
            n /= 2 # if n can be continually divided by 2 untill it equals 1 then it is a power of 2
        return n == 1