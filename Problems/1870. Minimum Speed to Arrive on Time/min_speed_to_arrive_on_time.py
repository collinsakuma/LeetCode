import math

class Solution:
    def minSpeedOnTime(self, dist, hour):

        # helper function to check if @ a specific speed we can get to 
        # work in the aloted hours
        def can_reach(speed):
            # initalize a variable to track the hours the trip has taken
            time_traveled = 0

            # loop through the range of the trains that we need to take
            for i in range(len(dist) - 1):
                # - for each train that is taken add the amount of time it take to
                #   ride that train
                # - use math.ceil() because trains only depart at the hour
                #   so if the train arive at 1.01 we will need to wait till 
                #   2 to take the next one 
                time_traveled += math.ceil(dist[i] / speed)
                # if our time traveled is greater than the hours we have to get
                # to work on time return False
                if time_traveled > hour:
                    return False
            
            # return true if we are can get work traveling at give speed on time or early
            return (time_traveled + (dist[-1] / speed)) <= hour
        
        # set min and max speed possible as variables
        min_speed, max_speed = 1, 10**7

        # set the ideal speed ( min speed that we can go to get to work on time )
        ideal_speed = -1

        # initalize the binary search
        while min_speed <= max_speed:
            # fin the mid speed between the min and max speed
            mid_speed = (min_speed + max_speed) // 2

            # check so see if we can get to work traveling at mid_speed
            if can_reach(mid_speed):
                # if we can set a new ideal speed and set a new max_speed to mid_speed - 1
                ideal_speed = mid_speed
                max_speed = mid_speed - 1
            # if we cannot reach work at the given speed
            else:
                # set a new minimum speed 
                min_speed = mid_speed + 1

        return ideal_speed