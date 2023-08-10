class Solution:
    def singleNonDuplicate(self, nums):
        # set two pointer variables for binary search
        begin = 0
        end = len(nums) - 1

        while begin < end: 
            mid = (begin + end) // 2
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # (mid % 2 == 1 and nums[mid - 1] == nums[mid])
                # - if mid is odd then its match should be at the index before it
                # (mid % 2 == 0 and nums[mid] == nums[mid + 1])
                # - if mid is even then its match sould be at the index after it
                begin = mid + 1
            else: # if neither conditon is met then the pattern is missed and the single number must occur before the mid point of the list
                end = mid
        return nums[begin]