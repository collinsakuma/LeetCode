class Solution:
    def destCity(self, paths):
        # deconstruct paths into a list of unique cities that are traveled too
        cities = set([city for path in paths for city in path])
        # loop though each travel path in paths
        for path in paths:
            if path[0] in cities: # if the city being left (index 0) is in the set of cities list
                cities.remove(path[0]) # remove that city from the list
            else: # if the city isnt in the list do nothing
                None
        # after removing starting cities from cities list there is only one city left, the destination city
        return list(cities)[0]