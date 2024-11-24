class Solution:
    ## first solution gets TLE with longer test cases
    def maximumSubarraySum(self, nums, k):
        max_subarray = 0 # maintain max length of subarray

        # loop through range of nums minus k
        for i in range(len(nums) - k + 1):
            # if there are no duplicate numbers in the subarray length k
            if len(set(nums[i:i+k])) == k:
                # check if its sum is a new max_subarray sum
                max_subarray = max(max_subarray, sum(max_subarray))

        return max_subarray # return the max sum of a subarray of length k
    
    ## second solution better than the first but still TLE
    # create a array that changes as the list of nums in itterated over 
    # check if new number is already in the list, if already there remove
    # numbers until dupilcate is removed
    def maximumSubarraySumTWO(self, nums, k):
        max_subarray = 0
        curr_sum = 0
        window = []

        # loop through nums
        for num in nums:
            # if the num is already in the list remove until no duplicate
            while num in window:
                removed = window.pop(0)
                # reduce current sum of the list
                curr_sum -= removed
            # if th current length of the list is k, remove one element and add the new one
            if len(window) == k:
                removed = window.pop(0)
                curr_sum -= removed
                window.append(num)
                curr_sum += num
            # add number to the list if not a duplicate or array not at length k
            else:
                window.append(num)
                curr_sum += num
            # if array is of length k check if its sum is a new max sum
            if len(window) == k:
                max_subarray = max(max_subarray, curr_sum)
        
        return max_subarray
    
    # third solution passes all test
    # use seen set instead of array of current numbers
    def maximumSubarraySumThree(self, nums, k):
        left, right = 0, 0
        max_sum, total = 0, 0

        seen = set()

        while right < len(nums):
            while nums[right] in seen:
                total -= nums[left]
                seen.remove(nums[left])
                left += 1

            total += nums[right]
            seen.add(nums[right])

            if (right - left + 1) == k:
                max_sum = max(max_sum, total)
                total -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            right += 1

        return max_sum