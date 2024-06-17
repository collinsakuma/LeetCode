import math

class Solution:
    def judgeSquareSum(self, c):
        # set two pointers
        # b is the sqareroot of c the max value that one side can be
        a, b = 0, int(math.sqrt(c))

        # whle a is less than b
        while a <= b:
            # if a^2 + b^2 == c return True
            if (a ** 2) + (b ** 2) == c:
                return True
            # if the sum of greater than c
            # increment the right side down
            elif (a ** 2) + (b ** 2) > c:
                right -= 1
            # if the sum is less than c
            # increment the left side up
            else:
                left += 1

        return False