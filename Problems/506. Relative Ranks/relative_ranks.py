import heapq

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
    
    def findRelativeRanksTwo(self, score):
        n = len(score)

        heap = []

        # add all the scores to a heap with their respective positional index in score array
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))

        # initalize a new array of length n
        ranks = [0] * n
        # start the places at 1st place
        place = 1

        # while heap continue to loop
        while heap:
            # set the positional index of the score
            starting_index = heapq.heappop(heap)[1]
            # if place is 1 through 3 give that person the medal
            if place == 1:
                ranks[starting_index] = 'Gold Medal'
            elif place == 2:
                ranks[starting_index] = 'Silver Medal'
            elif place == 3:
                ranks[starting_index] = 'Bronze Medal'
            # else set their position in string form
            else:
                ranks[starting_index] = str(place)
            place += 1
        
        return ranks