class Solution:
    def countSubarrays(self, nums, minK, maxK):
        output = 0
        # set starting index of current subarry to -1
        j = -1
        # initalize most recent index of min and max to -1
        prev_min_k_index = -1
        prev_max_k_index = -1

        for index, num in enumerate(nums):
            # if nums[index] out of range, move starting index of current subarray
            if num < minK or num > maxK:
                j = index
            
            # if nums[index] is minK, update most recent index of minK
            if num == minK:
                prev_min_k_index = index
            
            # if nums[index] is maxK, update most recent index of maxK
            if num == maxK:
                prev_max_k_index = index

            # add number of valid subarrays that end at index and add to output
            output += max(0, min(prev_min_k_index, prev_max_k_index) - 1)

        return output