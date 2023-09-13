class Solution:
    def candy(self, ratings):
        candies = [1] * len(ratings) # create new list the same length as ratings with the min amount of candies for each child

        # check each child against the child to the left
        for i in range(1, len(ratings)):
            # if the ratings for the child to the left is less than the current rating of i
            if ratings[i] > ratings[i - 1]:
                # set candies at i to one more than the child to the left
                candies[i] = candies[i - 1] + 1
        
        # loop though a second time checking each childs rating to the rating of the child to the right
        for j in range(len(ratings) - 2, -1, -1): # loop backwards
            # if ratings is higher than that of the rating to the child on the right
            if ratings[j] > ratings[j + 1]:
                # set candies of child j to which is greater the current count of candies at j or the child to the right candy count plus 1
                candies[j] = max(candies[j], candies[j + 1] + 1)

        return sum(candies) # return the sum of candies handed out