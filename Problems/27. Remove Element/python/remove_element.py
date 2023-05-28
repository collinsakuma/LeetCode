class Solution:
    def removeElement(self, nums, val):
        while val in nums:
        # While val exist in the list "nums" the loop with continue to run.
            nums.remove(val)
            # remove the first instance of val that is encountered.
        return len(nums)