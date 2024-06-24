class Solution:
    def minKBitFlips(self, nums, k):
        # create a coppy of array the same length as nums to track the spot in the list where we toggle the indexs
        acc, toggle = [0] * len(nums), 0

        for idx, num in enumerate(nums):
            # toggle the change digit if a flip interval has been left
            if idx >= k:
                toggle ^= acc[idx - k]
            # if num is not a 0 that needs to be flipped skip it
            if toggle != num:
                continue
            # if num is 0 that needs to be flipped but it is at an index
            # greater than k and therefore cannot be flipped anymore
            if k > len(nums) - idx:
                # return -1 because all digits cannot be flipped to 1
                return -1
            
            # num is a 0 that can be flipped to toggle it and record that it has 
            # been flipped in the acc list
            toggle ^= 1
            acc[idx] = 1

        # return the number of flips
        return sum(acc)