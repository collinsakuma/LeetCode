class Solution:
    def numRescueBoats(self, people, limit):
        # set two pointers front and back of the people list
        boat, low, high = 0, 0, len(people) - 1

        # sort the list of people in assending order
        people = sorted(people)

        # loop through pointers
        while low <= high:
            # - if the weight of the lighest and heaviest person at the curren location can share a boat
            # - increment the low side as the person has been paired
            # - if the two cannot be put on a boat together only increment the high side as they will
            #   boat the boat themself
            if people[high] + people[low] <= limit:
                low += 1
            # increment the number of boats 
            boat += 1
            # increment the high side down
            high -= 1

        return boat # return the number of boats used