class Solution:
    def findChampion(self, n, edges):
        # create undefeated dp
        is_undefeated = [True] * n

        # loop through matches
        for winner, loser in edges:
            # if the team is defeated flip them to False
            is_undefeated[loser] = False

        # set initial campion to -1
        champion = -1
        # count number of champions
        champion_count = 0

        # loop through teams
        for team in range(n):
            # if the team never lost set them to champion
            if is_undefeated[team]:
                champion = team
                # count the number of champions
                champion_count += 1

        # if there was only 1 champion return the champion
        if champion_count == 1:
            return champion
        
        return -1 # return -1 if there are multiple champions