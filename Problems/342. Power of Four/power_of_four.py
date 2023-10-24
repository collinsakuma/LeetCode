class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: # if n is less than or equal to 0 return False
            return False
        while n % 4 == 0: # continue while n modula 4 equals 0
            n //= 4 # divide n by 4
        return n == 1 # if n == 1 n is a power of 4