class Solution:
    # first solution only reduces by increments of 5 liters at a time
    def distanceTraveled(self, mainTank, additionalTank):
        distance = 0 # set variable to keep track of distance traveled
        while mainTank != 0: # while there is still gas in mainTank continue the loop
            if mainTank >= 5: # if there are more than 5 liters of gas in the main tank
                mainTank -= 5 # reduce mainTank by 5 liters
                disntace += 50 # increase the distance by the 10km per liter traveled (50km)
                if additionalTank > 0: # if there id fuel in the additionalTank add oneliter to the additional tank
                    mainTank += 1
                    additionalTank -= 1
            else: # if there is less than 5 liters left in the mainTank finish off the remaining fuel and add the remaining distance traveled
                distance += mainTank * 10
                mainTank -= mainTank
        return distance
    
    # second solution will reduce main tank by as many increments of 5 as possible at one time
    def distanceTraveledTwo(self, mainTank, additionalTank):
        distance = 0
        while mainTank != 0:
            if mainTank >= 5:
                used = mainTank // 5 # amount of 5 liter chunks that can be used at one time
                distance += (used * 5) * 10 
                mainTank -= (used * 5)
                mainTank += min(used, additionalTank) # add fuel from the additional fuel tank take the min number between the amount of 5 liter increments of gas that was used of the amount of additional liters of gas
                additionalTank -= min(used, additionalTank)
            else:
                distance += 10 * mainTank
                mainTank -= mainTank
        return distance