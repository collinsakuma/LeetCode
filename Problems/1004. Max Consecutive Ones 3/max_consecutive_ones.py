class Solution:
    def longestOnes(self, nums, k):
        left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0: # if the next number is a 0 deincrement k as 1 less 0 can be changed
                k -= 1
                # else dont change k
            
            if k < 0: # if k < 0 the left side of the window needs to be moved
                if nums[left] == 0: # if the furthest left index is a 0 adjust k by giving it back 1 operation
                    k += 1
                left += 1 # regardless of if left is a zero or 1 increment left
        return right - left + 1