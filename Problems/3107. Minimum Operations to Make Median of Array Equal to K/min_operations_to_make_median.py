class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        n = len(nums)
        mid = n // 2 # mid point ( location of median number )
        nums.sort()
        min_operations = 0

        # if median is k return no operations needed
        if nums[mid] == k:
            return 0
        
        # if median number is greater than k, traverse the left side
        if nums[mid] > k:
            for i in range(mid + 1):
                # adjust all number left of median to median number
                if nums[i] > k:
                    # add operations necessary
                    min_operations += nums[i] - k
        
        # if median number is less than k traverse the right side
        else:
            for i in range(mid, n):
                # adjust all numbers right of median to the median number
                if nums[i] < k:
                    min_operations += k - nums[i]

        return min_operations