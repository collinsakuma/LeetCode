from collections import Counter

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
    


    def bestHandTwo(self, ranks, suits):
        cnt = Counter(ranks) # dictionary method to keep track of each value in ranks and how many times each value appears in the list
        if len(set(suits)) == 1: # if a len of a set() of suits is only 1 index long that means that all values in the list where the same
            return "Flush"
        elif max(cnt.values()) >= 3: # if the max value of cnt is greater than or equal to 3 that means there is at least a three of a kind
            return "Three of a Kind"
        elif max(cnt.values()) == 2: # if max value of cnt is equal to 2 that means there is a two pair
            return "Pair"
        else:
            return "High Card"