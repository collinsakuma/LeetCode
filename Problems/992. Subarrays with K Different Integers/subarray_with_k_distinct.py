class Solution:
    def subarraysWithKDistinct(self, nums, k):
        # create an array to track the count of each number in the list
        count = [0] * (len(nums) + 1)
        output, i, j = 0, 0, 0

        for num in nums:
            # increase the count of the num in count array
            count[num] += 1

            if count[num] == 1:
                k -= 1
                if (k < 0):
                    count[nums[j]] = 0
                    j += 1
                    i = j
            if k <= 0:
                while count[nums[j]] > 1:
                    count[nums[j]] -= 1
                    j += 1
                output += j - i + 1
        
        return output