import functools

class Solution:
    def minimumTotalDistance(self, robot, factory):
        # sort the robots and factories by their position
        robot.sort()
        factory.sort()

        rl, fl = len(robot), len(factory)

        @functools.cache
        def dfs(i, j):
            # no more robots
            if i == rl:
                return 0
            # no more factores to assign 
            if j == fl:
                return float('inf')
            
            # try next factory
            cost = dfs(i, j + 1)

            # try current factory
            dist = 0
            n_robots = min(factory[j][1], rl - i)
            for k in range(n_robots):
                dist += abs(factory[j][0] - robot[i + k])
                cost = min(cost, dist + dfs(i + k + 1, j + 1))

            return cost
        
        return dfs(0, 0)