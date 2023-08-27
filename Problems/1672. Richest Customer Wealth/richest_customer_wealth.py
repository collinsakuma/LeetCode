class Solution:
    def maximumWealth(self, accounts):
        wealthiest = 0

        for acc in accounts: # loop through list of accounts
            if sum(acc) > wealthiest: # if the sum of the account is greater than the current wealthiest accounts 
                wealthiest = sum(acc) # set a new wealthiest account

        return wealthiest 