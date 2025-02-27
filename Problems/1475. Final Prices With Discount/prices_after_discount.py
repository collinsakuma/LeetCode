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
        # create output list
        output = [0 for _ in range(len(prices))]

        # loop through prices tracking their index
        for idx, price in enumerate(prices):
            # set final price to price initially
            output[idx] = price
            # loop through the discounts
            for discount in prices[idx + 1:]:
                # if a discount is less than the price apply the discount
                if discount <= price:
                    output[idx] -= discount
                    # break from loop becuase we only take the first lower discount 
                    # no the lowest discount possible
                    break
        return output