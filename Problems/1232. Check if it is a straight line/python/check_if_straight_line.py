class Solution:
    def checkStraightLine(self, coordinates):
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                # checking if the slope is the same
                # if slope not the same then coordinates do not represent a straight line. 
                return False
            
        return True