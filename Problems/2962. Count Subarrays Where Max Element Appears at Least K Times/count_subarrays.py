from collections import defaultdict

class Solution:
    def countSubarrays(self, nums, k):
        frequency = defaultdict(int)
        n = len(nums)
        # find the greatest number in nums
        max_element = max(nums)
        # initalize two pointers i and j
        # set a count to track the number of occurances of max_element in the window
        i, j, count, output = 0, 0, 0, 0

        while j < n:
            # if newest element in window is max_element increase its count
            if nums[j] == max_element:
                count += 1

            # if there are k or more occurances of max_element in the current window enter the inner loop
            if count >= k:
                # while there is equal or more occurances of max_elements in the window
                while count >= k:
                    # increase the count of possible subarrays 
                    output += n - j
                    # if the number leaving the window is equal to the max_element decrease its count by 1
                    if nums[i] == max_element:
                        count -= 1
                    # increment the window 
                    i += 1
            # increment the window
            j += 1
        
        return output
