class Solution:
    def largestAltitude(self, gain):
        altitude_arr = [0] # create an array with the height starting point of 0 as the first index
        altitude = 0 # set a starting altitude to 0
        for height in gain: # loop through the gain array
            altitude += height # add each height to the starting altitude of 0
            altitude_arr.apend(altitude) # after each height is added append the altitude to the array to keep track of the height after each gain
        return sorted(altitude_arr)[-1] # after all of the altitudes are recorded sort the altitude_arr and return the last index which is the highest point
    


    def largestAltitudeTwo(self, gain):
        curr_alt = 0 # variable to keep track of current altitude
        max_alt = 0 # variable to keep track of the heighest altitude reached
        for i in range(0, len(gain)):
            # loop through a range from 0 to the length of the gain arr
            curr_alt += gain[i] # each time through the loop add the height gain at index i to curr_alt
            max_alt = max(max_alt, curr_alt) # each time through the loop compare the curr_alt to the max_alt and set max_alt to which is higher
        return max_alt # after are indexes have been looped through return the max_alt
    
    def largestAltitueThre(self, gain):
        max_altitude = 0
        curr_altitude = 0

        for i in gain:
            curr_altitude += i
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude