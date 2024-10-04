import math

class Solution:
    def dividePlayers(self, skill):
        n = len(skill) // 2 # number of teams 

        team_skill = math.inf # set inital skill of teams to infinity
        chemistry = 0 # set initial chemistry to 0

        # loop through number of teams
        for _ in range(n):
            # always pair least and most skilled player together
            a, b = skill.pop(0), skill.pop(-1)

            # for the first pair do not compare to team skill
            if team_skill == math.inf:
                # add teams chemistry to total
                chemistry += (a * b)
                # set a new team skill that all other teams must equal
                team_skill = (a + b)
            # check if team skill is the same for all teams
            else:
                # if the team skill do not match return -1 
                if team_skill != (a + b):
                    return -1
                # if team skills match add their chemistry to the total
                else:
                    chemistry += (a * b)

        return chemistry