class Solution:
    def finalPrices(self, prices):
        final_price = prices # create a copy of prices to apply discounts too

        for i in range(len(prices) - 1): # loop though range of len(prices), minus 1 is because last price cannot have a discount
            for j in prices[i + 1:]: # loop though all prices after i
                if prices[i] >= j: # if current price being looked at is greater than or equal to price j then the discount price has been found
                    final_price[i] = prices[i] - j # change price by price[i] - j (the discount)
                    break # exit second loop as the discount has been found for i
        return final_price 
    
    # second solution question of the day 12/18/2024
    def finalPricesTwo(self, prices):
        output = [0 for _ in range(len(prices))]

        for idx, price in enumerate(prices):
            output[idx] = price
            for discount in prices[idx + 1:]:
                if discount <= price:
                    output[idx] -= discount
                    break
        return output