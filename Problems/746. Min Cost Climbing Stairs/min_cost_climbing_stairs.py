class Solution:
    def minCostClimbingStairs(self, cost):
        curr = 0 # set a current value for the step that we are on
        dp_0 = cost[0] # set first cost to the 0 index of cost

        if len(cost) >= 2:
            dp_1 = cost[1]

        for i in range(2, len(cost)): # loop though range starting at 2 because the first two values have been set
            # break the problem down in to subproblem, to get to index(i) we choose the min between dp_0, and dp_1
            curr = cost[i] + min(dp_0, dp_1)
            dp_0 = dp_1 # set new dp_0
            dp_1 = curr # set new dp_1 

        return min(dp_0, dp_1) # return the minimum cost to get to the last step