class Solution:
    def maxSubsequence(self, nums, k):
        # while the list is greater than desired subsequence length continue to loop
        while len(nums) > k:
            # remove the smallest number in nums
            nums.remove(min(nums))
        return nums # after nums is of length k return nums