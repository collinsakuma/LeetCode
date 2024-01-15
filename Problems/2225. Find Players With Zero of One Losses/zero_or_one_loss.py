class Solution:
    def findWinners(self, matches):
        answer = [[], []] # answer[0] list of players with zero losses, answer[1] list of players with 1 loss only
        players = dict() # initalize a dictionary to keep track of players and their losses

        for match in matches: # loop though each match played
            # if the winner of the match is not in the dictionary, add them to the to the dict with player number as key and 0 as value, ( 0 to represent zero losses )
            if match[0] not in players:
                players[match[0]] = 0
            # if the loser of the match is not in the dictionary, add them to the dictionary with 1 as the value, ( representing their loss )
            if match[1] not in players:
                players[match[1]] = 1
            # if the player who lost the match is already in the dicitonary incrase their loss count by 1
            else:
                players[match[1]] += 1
        
        # loop though each player in the dict key = player number, value = number of losses
        for key, value in players.items():
            # if the player has 0 losses add them to the list of players with no losses
            if value == 0:
                answer[0].append(key)
            # if the player has 1 loss add them to the list of players with 1 loss
            if value == 1:
                answer[1].append(key)
        
        # solution calls for the players to be in order 
        answer[0], answer[1] = sorted(answer[0]), sorted(answer[1])

        return answer
