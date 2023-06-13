class Solution:
    def findNonMinOrMax(slef, nums):
        if len(nums) <= 2: # if the nums list has 2 or less elements
            return -1
        return sorted(nums)[-2]
        # sorted() method puts the nums list in order and [-2] selects the second to last element in the list
        # ensuring that the smallest or largest number is not returned but one between the two. 