class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate) # get the number of senators before sorting into party

        # create two sorted arrays for Radiant and Dire senators. 
        radiant_que = [i for i in range(len(senate)) if senate[i] == "R"]
        dire_que = [j for j in range(len(senate)) if senate[j] == "D"]

        while radiant_que and dire_que:
            # while both radiant and dire ques are true (exist)
            radiant = radiant_que.pop(0) # pop out the first index 
            dire = dire_que.pop(0)
            if radiant < dire:
                # if the value poped from the radiant array is greater than the value poped from the dire array
                # then add a new value to the end of the radiant array.
                radiant_que.append(n + radiant)
            else:
                dire_que.append(n + dire)
        return "Radiant" if radiant_que else "Dire"
        # the while loop will stop when either radiant_que or dire_que run out of indexes
        # return the party that still has values in its array ( the winning party )


    def predictPartyVictoryNoCheating(self, senate):
    # first solution I came up with passes many test cases but not all
    # logic is too simple and many cases will give wrong output.
    # for Example:
    #   if senate = "DDRRR"
    #   1. in first round senate[0][1] will skip the first two Radiants
    #   2. senate[4] can only skip one Dire(senate[0])
    #   3. in the second round senate[1] the Dire will skip the only remaining Radiant seante[4]
    #   Meaning the Dires will win the vote. 
    #   this formula will incorrectly return Radiant beacuse there are three Radiants as opposed to two Dires.
        radiant_count, dire_count = 0, 0
        for letter in senate:
            if letter == "R":
                radiant_count += 1
            elif letter == "D":
                dire_count += 1
        if radiant_count == dire_count:
            if senate[-2] == "R":
                return "Radiant"
            return "Dire"
        elif radiant_count > dire_count:
            return "Radiant"
        return "Dire"