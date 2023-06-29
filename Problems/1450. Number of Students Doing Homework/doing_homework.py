class Solution:
    def busyStudent(self, startTime,endTime, queryTime):

        output = 0 # variable to keep track of students doing homework at specified queryTime

        for i in range(len(startTime)): # start a loop that will run for as many students there are 
            if queryTime == startTime[i] or queryTime == endTime[i]: # if the queryTime is either the hour the student is starting or ending add 1 to output
                output += 1
            elif queryTime in range(startTime[i], endTime[i]): # check if the query time is in the range of student i's start or end time
                output += 1
        return output # return the number of students doing homework during the queryTime hour.