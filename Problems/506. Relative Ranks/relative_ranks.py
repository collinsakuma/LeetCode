class Solution:
    def findRelativeRanks(self, score):
        # create a copy of scores sorted in reverse order
        sorted_score = sorted(score)[::-1]
        place = [] # list to return with the place of each particapants
        for i in score: # loop though scores
            current_place = sorted_score.index(i) # set a variable with the index of each score in the sorted list
            # first check if the score is in the top three scores if so append the medal earned
            if current_place == 0:
                place.append("Gold Medal")
            elif current_place == 1:
                place.append("Silver Medal")
            elif current_place == 2:
                place.append("Bronze Medal")
            else: # if participant is not in medal position return the place they are in
                place.append(str(current_place + 1))
        
        return place # return list of places