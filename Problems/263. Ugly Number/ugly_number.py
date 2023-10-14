class Solution:
    def isUgly(self, n):
        # check chase if num == 0 return False 
        if n == 0:
            return False
        while n % 5 == 0: # while n is still divisible by 5 divide n by 5
            n /= 5
        while n % 3 == 0: # while n is still divisible by 3 divide n by 3
            n /= 3
        while n % 2 == 0: # while n is still divisible by 2 divide n by 2
            n /= 2
        return n == 1 # return n if n equals 1