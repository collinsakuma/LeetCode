class Solution:
    def passThePillow(self, n, time):
        # set the initial direction to positive
        direction = 1
        # start at person 1
        index = 1

        # while there is still time to pass the pillow continue 
        while time:
            # pass the pillow in the direction 
            index += direction

            # if we have reached the last person, reverse the direction to pass back the other way
            if index >= n:
                direction = -1
            
            # if we reach the first person again reverse the direction again
            if index == 1:
                direction = 1

            time -= 1 # reduce the time after the pillow is passed

        return index # return the index of the last person who has the pillow