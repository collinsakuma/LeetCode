class Solution:
    def longestSubarray(self, nums):
        longest = curr = mx = 0
        # loop through nums
        for num in nums:
            # if new max number set new max
            if num > mx:
                mx = num
                # set longest and curr equal to 1
                longest = curr = 1
            # if number and max are equal
            elif num == mx:
                # increment curr
                curr += 1
                # check for new longest
                longest = max(longest, curr)
            else:
                # reset curr to 0
                curr = 0
        return longest