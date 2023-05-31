from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkInMap = {} # create an empty dict that will hold each users checkin data. 
        self.routeTotalTime = defaultdict(int) # empty dict to store total time for each route. 
        self.routeCount = defaultdict(int) # empty dict to store the total number of times each route has been taken. 

    def checkIn(self, id, stationName, t):
        self.checkInMap[id] = [stationName, t]
        # adds an entry to the checkInMap dict where id is the key and the station name and time are the values.

    def checkOut(self, id, stationName, t):
        checkIn = self.checkInMap.pop(id)
        # removes the checkIn information for the user with the given id and saves it into the checkIn variable. 
        routeName = (checkIn[0], stationName)
        # creates a tuple with the checkIn stationName and the checkOut StationName. 

        self.routeTotalTime[routeName] += t - checkIn[1]
        # update the routeTotalTime dict for the specific route(routeName) subtracting the check-in time from the check-out time.
        self.routeCount[routeName] += 1
        # routeCount increments the amout of times that routeName has been traveled by 1. 

    def getAverageTime(self, startStation, endStation):
        routeName = (startStation, endStation) # creates a tuple of the route (startStation, endStation) used as the key for the dicts. 
        return self.routeTotalTime[routeName] / self.routeCount[routeName]
        # return the totalTime from the dict with key of routeName and divide it by the amount of times that route has been traveled
        # to return the average travel time for that route. 

class UndergroundSystemSolutionTwo:
    
    def __init__(self):
        self.checkedIn = dict() # dict to keep track of passenger checkin information
        self.timeTrack = dict() # dict to keep track of time spent between stations (travel time), and the number of times a particular route has been traveled.

    def checkIn(self, id, stationName, t):
        if id not in self.checkedIn:
        # check if there is already a value for that id. 
            self.checkedIn[id] = (stationName, t)
            # create an entry to the checkedIn dict with passanger Id as the key and a tuple with station name and check-in as the value.
        else:
            raise ValueError
        
    def checkOut(self, id, stationName, t):
        if id not in self.checkedIn:
            raise ValueError
        else:
            startStation, startTime = self.checkedIn.pop(id)
            # pops values from the checkedIn dict at the key of id
            key = (startStation, stationName)
            # creates a key tuple with the values from checkIn.pop(id)
            total, count = self.timeTrack.get(key, (0,0))
            # .get() method used to retrieve the values for the total and count at the key of key(startStation, stationName)
            # if entry does not exist (no trips between those two specific stations have been made yet) it return a default 
            # value of (0, 0) assigned to the variables total and count. 
            self.timeTrack[key] =(total + t - startTime, count + 1)
            # updates the timeTrack dict by adding to the total duration and incrementing the count by 1 for the key 
            # representing the trip.  
        
    def getAverageTime(self, startStation, endStation):
        num, den = self.timeTrack.get((startStation, endStation), (0,1))
        # gets the values of from the dict timeTrack at the key of (startStation, endStation) and sets them to num & den
        return num / den
        # return the averageTime to travel between two stations by dividing the total time traveled between the two / by the amount of
        # times that route has been taken. 