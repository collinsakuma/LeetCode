class Solution:
    def minimumCost(self, cost):
        min_cost = 0
        cost = sorted(cost) # sort the costs in assending order

        while len(cost) >= 3: # while there are 3 or more candies left start loop
            # remove the two most expensive candies (last 2 indexes) from cost adding their cost to min_cost
            min_cost += cost.pop(-1)
            min_cost += cost.pop(-1)
            # after two most expesive candies bought, remove the third candy for free
            cost.pop(-1)
        # if there is less than 3 candies left in cost, add the remaining cost to min_cost as none can be had for free
        min_cost += sum(cost)

        return min_cost # return min_cost