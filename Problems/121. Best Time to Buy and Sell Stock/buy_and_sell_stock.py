class Solution:
    def maxProfit(self, prices):
        max_profit = 0 # set max profit variable to track the max profit that can be made from buying and selling the stock optimaly
        min_purchase = prices[0] # set the minimum purhcase price possible, set to the first price in the list

        for i in range(1, len(prices)): # loop though the range of length prices starting at the second price as price[0] is already set as the first min_purchase price
            # check for a new max profit of selling the stock at price i
            max_profit = max(max_profit, prices[i] - min_purchase)
            # check for a new lower price to buy the stock at, at index i
            min_purchase = min(min_purchase, prices[i])

        return max_profit # return the max profit attainable or 0 if no profit can be made