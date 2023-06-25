class Solution:
    def numberOfMatches(self, n):
        
        remaining_teams = n # create a variable to keep track of teams remaining in the tournament
        rounds_played = 0 # create a variable to keep track of rounds played in the tournament

        if n == 1: # if the number of teams == 1 then no games are played
            return 0
        
        while remaining_teams != 0: # start a loop that will continue untill there are no teams remaining in the tournament i.e. tournament is over
            if remaining_teams == 2: # if there are only two teams left add 1 round to the count and remove both teams from the remaining_teams
                rounds_played += 1
                remaining_teams -= 2
            elif remaining_teams % 2 != 0: # if there is an odd number of teams in the tournament. One team is automatically advanced to next round
                rounds_played += (remaining_teams - 1) / 2 
                remaining_teams = ((remaining_teams - 1) / 2) + 1 
            else: # if there are an even number of teams then rounds played and remaining teams are both divided by 2
                rounds_played += (remaining_teams / 2)
                remaining_teams = (remaining_teams / 2)
        return int(rounds_played) # return the number of games that are played thoughout the tournament
    
    def numberOfMatchesTwo(self, n):
        return n - 1 # Solution from leetcode. 