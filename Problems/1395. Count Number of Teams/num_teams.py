class Solution:
    def numTeams(self, rating):
        n = len(rating)

        up = [0] * n
        down = [0] * n

        teams = 0

        for i in range(n):
            for j in range(j):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]

                else:
                    down[i] += 1
                    teams += down[j]

        return teams