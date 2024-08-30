from collections import defaultdict

class Solution:
    def removeStones(self, stones):
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        points = {(i,j) for i, j in stones}

        for i, j in stones:
            x_dict[i].append(j)
            y_dict[j].append(i)

        def remove_points(a,b):
            points.discard((a,b))
            for y in x_dict[a]:
                if (a,y) in points:
                    remove_points(a,y)

            for x in y_dict[b]:
                if (x,b) in points:
                    remove_points(x,b)

        count = 0

        for a,b in stones:
            if (a,b) in points:
                remove_points(a,b)
                count += 1

        return len(stones) - count