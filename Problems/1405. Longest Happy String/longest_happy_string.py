import heapq

class Solution:
    def longestDiverseString(self, a, b, c):
        pq = [] # initalize heap

        # add each letter to the heap only if its count is greater than 0
        # add using negative because we want greatest value first
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        output = '' # initalize the longest happy string

        # while heap
        while pq:
            # pop the greatest value
            most = heapq.heappop(pq)
            # if the length of the output string is greater than 2 
            # and the two most recent letter are equal to the letter in most
            if len(output) >= 2 and output[-1] == output[-2] == most[1]:
                # if there are no letter left in the heap break fromt he loop
                if not pq:
                    break
                # pop the letter with the second most occurances left
                second_most = heapq.heappop(pq)
                # add the second most common letter to the heap
                output += second_most[1]
                # decrease the count of the second most letter
                second_most = (second_most[0] + 1, second_most[1])
                # if the count of that letter is not 0 add it back to the heap
                if second_most[0] != 0:
                    heapq.heappush(pq, second_most)
                # add the letter with the most left back to the heap
                heapq.heappush(pq, most)
            else:
                # add the letter with the most occurances left to the string
                output += most[1]
                # increment the number of that letter down 
                most = (most[0] + 1, most[1])
                # if there are still occurances of that letter left to add, add it back to the heap
                if most[0] != 0:
                    heapq.heappush(pq, most)
        
        return output