class Solution:
    def heightChecker(self, heights):
        # create a sorted versions of the heights list
        ordered_heights = sorted(heights)
        # track the number of people that are out of order
        changes = 0

        # loop through a range of the length of heights
        for i in range(len(heights)):
            # if the heights are not equal then the person is out of order
            if heights[i] != ordered_heights[i]:
                # increment changes
                changes += 1
        
        # return the count of people who are out of order
        return changes