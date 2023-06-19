class Solution:
    def largestAltitude(self, gain):
        altitude_arr = [0] # create an array with the height starting point of 0 as the first index
        altitude = 0 # set a starting altitude to 0
        for height in gain: # loop through the gain array
            altitude += height # add each height to the starting altitude of 0
            altitude_arr.apend(altitude) # after each height is added append the altitude to the array to keep track of the height after each gain
        return sorted(altitude_arr)[-1] # after all of the altitudes are recorded sort the altitude_arr and return the last index which is the highest point