class Solution:
    def maximumHappinessSum(self, happiness, k):
        # sort list in descending order
        happiness.sort(reverse=True)
        i = 0
        res = 0

        # while there are children to selcet continue to loop
        while k > 0:
            # choose the child with the greatest happiness at index i, 
            # set the happiness at that index to the which ever value is greater that happiness minus how many children have been picked ( account for decreasing happiness )
            # or 0 if the happiness would be less than 0
            happiness[i] = max(happiness[i] - i, 0)
            # add the happiness to the answer
            res += happiness[i] 
            # increment the index of child to be looked at next
            i += 1
            # reduce the number if children that need to be picked k
            k -= 1
        
        return res