class Solution:
    def maxProfit(self, prices, fee):
        buy = float('-inf') # initialize a starting buy variable. use -inf to make sure that forst price is a valid buy
        sell = 0

        for price in prices: # loop through the prices
            buy = max(buy, sell - price) # for each price set buy to the maximun value of either the first buy, or the sell - the current price
            sell = max(sell, buy + price - fee) # for each price set the sell to the maximun value of either the current sell or the buy value - price - transaction fee

        return sell
