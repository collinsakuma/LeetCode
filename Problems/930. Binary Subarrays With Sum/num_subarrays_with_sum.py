from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums, goal):
        # output is a dictionary that will store count of subarrays that have a certaion prefix sum
        output = defaultdict(int)
        # initalize with 1 because when a prefix sum equals the goal we have found 1 subarray
        # EXAMPLE ## if prefix_sum = 2 and the goal is 2 then a subarray that equals the goal has been found
        output[0] = 1
        # count of subarrays that equal the goal
        subarrays = 0
        # store cumulative sum of elements encountered
        prefix_sum = 0

        # loop through elements in nums
        for i in nums:
            # increment the sum of elements by i
            prefix_sum += i 
            # update subarrays by count of subarrays found so far whose sum equals to prefix_sum - goal
            subarrays += output[prefix_sum - goal]
            # increment dict with the count for the current prefix_sum
            output[prefix_sum] += 1
        return subarrays
    
#### EXAMPLE BELLOW ####
# print(Solution.numSubarraysWithSum(None,nums=[1,0,1,0,1],goal=2))
# Iteration 1 (i = 1)
#   prefix_sum = 1
#   subarrays = 0
#   output = {0:1, 1:1}

# Iteration 2 (i = 0)
#   prefix_sum = 1
#   subarrays = 0
#   output = {0:1, 1:2}

# Iteration 3 (i = 1)
#   prefix_sum = 2
#   subarrays = 1  <---- increase subarrays because a subarray that equal the goal has ben found [1,0,1]
#   output = {0:1, 1:2, 2:1}   

# Iteration 4 (i = 0)
#   prefix_sum = 2
#   subarrays = 2 <---- subarrays is again incrased by 1 because a entry in output has been found where prefix_sum - goal = 0
#   output = {0:1, 1:2, 2:2} <--- 2:X is incremented because this is the second time a prefix_sum of 2 has been encountered

# Iteration 5 (i = 1)
#   prefix_sum = 3
#   subarrays = 4 <--- subarrays is increased by 2 because prefix_sum - goal (3 - 2) = 1, the prefix sum of 1 has been encountered 2 times before so increase the subarray count by 2
#   output = {0:1, 1:2, 2:2, 3:1} 