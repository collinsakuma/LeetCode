class Solution:
    def pivotInteger(self, n):
        right = n * (n + 1) // 2 # formula to sum 1 through n if n = 5 (5 * (5 + 1) // 2) is the same as 1 + 2 + 3 + 4 + 5
        left = 0 # set left to 0 because for first iteration there is no numbers to the left

        for i in range(n, n + 1): # loop throught range from 1 to n + 1
            right -= i # do not include the current number i only want sums of numbers to the rigth or left of it
            if left == right: # if both sides are equal return i pivot number has been found
                return i
            left += i # if pivot number not found reduce left by i for next iteration
        return -1