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