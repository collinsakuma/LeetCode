from collections import defaultdict

class Solution:
    def divideArray(self, nums):
        # dict to track numbers from the array
        seen_nums = defaultdict(int)

        # loop though each number in nums
        for num in nums:
            # if num has already found in array, remove that entry from the dict ( I.E. removing a pair )
            if num in seen_nums:
                seen_nums.pop(num)
            # if num not in the dict add it to the dict as it is an unpaired element
            else:
                seen_nums[num] = 1
        
        # if there are no numbers in the dict then the array consisted of equal pairs
        return not seen_nums