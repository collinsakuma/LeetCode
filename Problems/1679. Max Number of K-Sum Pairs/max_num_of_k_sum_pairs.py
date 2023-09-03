class Solution:
    def maxOperations(self, nums, k):
        nums.sort() # sort numbers in assending order
        # set two pointers start and end
        start, end = 0, len(nums) - 1
        pairs = 0

        while start < end: # while start is less than end conntinue the loop
            pair_sum = nums[start] + nums[end] # find the sum of the two points
            if pair_sum == k: # if the sum of the pair equals k then a pair has been found
                pairs += 1 # increase the pairs by 1
                # increment both start and end 
                start += 1
                end -= 1
            elif pair_sum < k: # if pair_sum is less than k, increment only the start, because the list is sorted the smallest number is at the beinging and largest number is at the end 
                start += 1
            else: # if pair_sum is greater than k, increment only the end pointer
                end -= 1
        return pairs