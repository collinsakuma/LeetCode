import math

class Solution:
    def nearestValidPoint(self, x, y, points):
        # set initial variable for nearest to infinity, replace as nearer dinstances are found
        # set index variable to keep track of index of the nearest point
        nearest, index = math.inf, 0

        for num, i in enumerate(points): # loop though points using enumerate() to keep track of the index of each point
            # only check distance if the x or y coordinate matches i's coordinates
            if x == i[0] or y == i[1]:
                # check the Manhattan distance(abs(x1 - x2) + abs(y1 - y2)) from i to the given coordinates 
                if abs(x - i[0]) + abs(y - i[1]) < nearest:
                    # if the Manhattan distance is less than the current nearest distance
                    # set new nearest distane and set new index to the index of i
                    nearest = abs(x - i[0]) + abs(y - i[1])
                    index = num
        
        if nearest == math.inf:
            # if nearest is still infinity return -1
            return -1 
        else: # return index of nearest point otherwise
            return index