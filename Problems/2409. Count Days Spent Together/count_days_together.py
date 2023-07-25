class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):

        def convertDate(travelDate): # separe function to convert the date in "XX-XX" form to a number that represents the day of the year
            monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            month = int(travelDate[:2]) # get the month from the first two indexes of the string [:2]
            days = int(travelDate[3:]) # get the day of the month from the indexes starting at index 3 to the end of the string [3:]
            return sum(monthList[: month - 1]) + days # return the sum of all of the months up to month and add the extra days to get the date in x/365
        
        return max(0, convertDate(min(leaveAlice, leaveBob)) - convertDate(max(arriveAlice, arriveBob)) + 1)
        # return the value when converting the dates of min(leaveAlice, leaveBob) "whoever left first" - the value of the max(arriveAlice, arriveBob)