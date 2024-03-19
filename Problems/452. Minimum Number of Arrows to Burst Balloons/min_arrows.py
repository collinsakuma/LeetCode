class Solution:
    def findMinArrowShots(self, points):
        points = sorted(points) # sort the balloons
        arrows = 1 # min number of arrows needed to shoot balloons is 1
        aim_at = points[0][1] # aim the first arrow at the right most point of the first balloon

        # loop though all balloons
        for balloon in points:
            # check if the next balloon doesnt overlap with the right most point of the balloon before
            if balloon[0] > aim_at:
                # a new arrow is needed to shoot this balloon increment arrows by 1
                arrow += 1
                # set a new right most point of aim for the new arrow
                aim_at = balloon[1]
            else:
                # if the balloon can be shot with the same arrow, set a new aim_at point either the right most point of either balloon
                aim_at = min(aim_at, balloon[1])
        return arrows