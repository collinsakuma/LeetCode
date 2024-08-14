import math

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

### created guess API that knows that the picked number is and passes if
### if it is higher lower of equal to the guess number function
class GuessAPI:
    def __init__(self, pick):
        self.pick = pick

    def guess(self, num):
        if num == self.pick:
            return 0
        elif num > self.pick:
            return -1
        else:
            return 1


class Solution:
    def guessNumber(self, n):
        # set the min and max numbers 
        min_num, max_num = 0, n
        # set an inital value for the number check function
        num_check = -math.inf

        # while the number is still not the picked one continue the loop
        while num_check != 0:
            # find the mid point between the two points
            mid = min_num + ((max_num - min_num) // 2)
            # check if mid is the correct number
            num_check = GuessAPI.guess(mid)

            # if mid point is less than the picked number set a new floor boundary
            if num_check == 1:
                min_num = mid + 1
            # if mid point is greater than the picked number set a new cieling boundary
            else:
                max_num = mid

        return mid # return the mid number once guess() return 0