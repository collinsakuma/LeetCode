class Solution:
    def isArraySpecial(self, nums):
        # loop through range of length nums starting from the second index
        for i in range(1, len(nums)):
            # if current number and previous number have the same mod 2 then
            # adjacent pairs does not have different parities
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        # if loop finishes then all pairs have different parities
        return True