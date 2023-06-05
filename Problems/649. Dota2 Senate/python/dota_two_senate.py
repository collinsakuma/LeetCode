class Solution:
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