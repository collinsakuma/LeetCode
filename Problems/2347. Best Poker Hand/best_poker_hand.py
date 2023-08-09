class Solution:
    def bestHand(self, ranks, suits):
        # if any suit appears 5 times in the suits array return that you have a Flush
        if suits.count("a") == 5 or suits.count("b") == 5 or suits.count("c") == 5 or suits.count("d") == 5:
            return "Flush"
        for num in ranks: # if the same number appears 3 or more times in the array then we have a three of a kind or better
            if ranks.count(num) >= 3:
                return "Three of a Kind"
        for num in ranks: # if the same number appears twice in the ranks array they we have achieved a two pair
            if ranks.count(num) == 2:
                return "Pair"
        return "High Card" # if no other out comes have been reached then return that we have a high card