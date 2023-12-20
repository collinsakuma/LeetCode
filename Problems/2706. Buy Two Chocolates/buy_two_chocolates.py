class Solution:
    def buyChoco(self, prices, money):
        prices = sorted(prices) # sort prices from lowest to highest

        # sum of two lowest prices
        two_cheepest = prices[0] + prices[1]
        
        if two_cheepest <= money: # if the two cheepest chocolates can be bought return the money left over
            return money - two_cheepest
        return money # if two chocolates cant be purchased return the original amount of money