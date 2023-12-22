class Solution:
    def maxWidthOfVerticalArea(self, points):
        x_points = [] # empty list that will contain all of the x coordinates of the points
        max_dist = 0 # set a variable to keep track of the max distance between two points

        for coordinates in points: # loop though each coordinates in the points list
            x_points.append(coordinates[0]) # append the x coordinate to the list of x_points
        
        x_points = x_points.sorted(x_points) # sort the list of x coordinates

        for j in range(len(x_points) - 1): # loop though a range of length x_points
            dist = x_points[j + 1] = x_points[j] # find the distance between adjacent points
            if dist > max_dist: # if there is a new max distance found set a new max_dist
                max_dist = dist

        return max_dist # return the greatest distance between two points