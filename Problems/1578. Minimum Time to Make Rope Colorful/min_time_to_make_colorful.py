class Solution:
    def minCost(self, colors, neededTime):
        ans = prev = 0
        # loop though range of length colors
        for i in range(1, len(colors)):
            # check if colors are the same and if one needs to be removed
            if colors[prev] != colors[i]:
                prev = i # if colors are not the same increment to next balloon
            else: # if colors are the same determine which one to remove
                ans += min(neededTime[prev], neededTime[i]) # remove the balloon with the minimum time to remove it
                if neededTime[prev] < neededTime[i]: # if the time to remove the current one is greater than the time to remove the previous balloon set the current to ballon to prev
                    prev = i
        return ans