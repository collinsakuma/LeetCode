class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        # set two variables to keep track of the longest time waited so far and the index of that key
        time = releaseTimes[0]
        index = 0

        for i in range(1, len(releaseTimes)): # loop through range of the release times starting at 1
            if time == (releaseTimes[i] - releaseTimes[i - 1]): # if the wait time is the same as the current longest
                if ((ord(keysPressed[index]) - 96) < (ord(keysPressed[i]) - 96)): # find the letter that is larger lexoconically
                    index = i # if i is lexiconically greater than the current index set i as the new index
            if time < (releaseTimes[i] - releaseTimes[i - 1]): # if current longest time waited is less than the new time waited for key i
                time = releaseTimes[i] - releaseTimes[i - 1] # set a new time
                index = i # set a new index
        return keysPressed[index] # return the letter at the index of index of keysPressed