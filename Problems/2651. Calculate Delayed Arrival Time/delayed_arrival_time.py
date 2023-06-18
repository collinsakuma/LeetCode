class Solution:
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        return (arrivalTime + delayedTime) % 24
        # find the remainder of arrivalTime + delayedTime when divided by 24
        # Example:
        #   arrivalTime = 15, delayedTime = 10
        #   15 + 10 % 24 will return 1 meaing that the new arrival time is 1am
        #   if arrivalTime = 23, delayedTime = 24
        #   23 + 24 % 24 will return 23 because the arrival is delayed by a whole day