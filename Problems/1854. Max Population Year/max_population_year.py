class Solution:
    def maximumPopulation(self, logs):

        max_year = 0 # variable to keep track of year with the max population
        num_alive = 0 # variable to keep track of the max number of people alive in the max_year

        for year in range(1950, 2050): # loop through the range of years give. 
            curr = 0 # set a curr variable to keep track of how many people are alive in the current year

            for log in logs:
                if year in range(log[0],log[1]): # for each log in logs check if that person was alive during the current year
                    curr += 1 # if that log ( person ) was alive during that year add one to the curr count
            if curr > num_alive: # after the logs have been looped though for the year check if the curr is greater than the current max number
                # if the value of curr is greater set a new max_year where there was the most people alive at once
                max_year = year
                num_alive = curr
        return max_year # after looping though all the years return the max_year 