class Solution:
    def eliminateMaximum(self, dist, speed):
        time_from_city = [] # create a list to add the time it will take each monster to get to the city

        for i in range(len(dist)): # loop through a range of length distances
            time_from_city.append(dist[i] / speed[i]) # find the time it will take each monster i to get to the city and add that to the list

        time_from_city.sort() # sort the list in order of which monster will get to the city first

        for j in range(len(time_from_city)): # loop a second time 
            if time_from_city[j] <= j: # if the amount of time the monster will take to get to the city if less than or equal to its index position they you will lose
                return j # return j, j represents the number of monsters eliminated even though index j is not eliminated it accounts for 0 indexing
        
        return len(dist) # return len(dist) because all monsters have been eliminated