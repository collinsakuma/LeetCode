import math

class Solution:
    def bestClosingTime(self, customers):
        # set penalty variable initially to infinity as it will be replace by the smallest possible penalty
        penalty, penalty_hour = math.inf, 0
        hour = 0
        # start a loop that increments hours to check the penalty if the store is closed at each hour
        while hour < len(customers) + 1:
            pen = 0 # set penalty for being closed at this hour to 0
            # separate the string into hours that the store will be open and hours the store will be closed
            is_open = customers[:hour] 
            is_closed = customers[hour:]
            # first count how many hours the store is open and no customers enter the store
            pen += is_open.count("N")
            # second count how many hours the store is closed and would have had customers enter the store
            pen += is_closed.count("Y")

            if pen < penalty: # if pen is lower than the current lowest penalty 
                penalty = pen # set a new lowest penatly score
                penalty_hour = hour # set a new hour for the lowest penalty
            hour += 1
        
        return penalty_hour # return the hour that the store should close to incure the smallest penalty