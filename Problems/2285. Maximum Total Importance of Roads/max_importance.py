class Solution:
    def maximumImportance(self, n, roads):
        roads_list = [0] * n
        total_score = 0

        # count the amount of connections each road has
        for a, b in roads:
            roads_list[a] += 1
            roads_list[b] += 1

        # sort the roads
        roads_list.sort()

        # find the score of each road
        for i in range(len(roads_list)):
            total_score += roads_list[i] * (i + 1)

        return total_score