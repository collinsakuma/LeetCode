class Solution:
    def kLengthApart(self, nums, k):
        first_one = 1 # flag to show if the first one in nums has been iterated though yet, when found switch to 0
        for i, num in enumerate(nums):
            if num == 1 and first_one: # find the first instance of 1 and trigger the flag (first_one) to 0
                first_one = 0
                last_index = i # set the index of the 1 to a variable to track when it was last seen
            elif num == 1: # if num equals 1 and it is not the first 1
                if i - last_index <= k: # check if this and the last 1 are k places apart
                    return False # if not k places apart return False
                last_index = i # set new last_index

        return True # return True if all 1's are k places apart