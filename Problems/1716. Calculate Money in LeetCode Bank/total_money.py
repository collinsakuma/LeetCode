class Solution:
    def totalMoney(self, n):
        # if there is less than 1 full week of days to add money
        if n <= 7:
            return n * (n + 1) // 2
    
        weeks = n // 7 # find the total number of whole weeks
        money = weeks * 28 # every week a total of $28 is saved plus 7 * what week it is after the first
        money += (weeks * (weeks - 1) * 7) // 2

        if n % 7 != 0:
            days = n % 7
            day = weeks + 1
            for j in range(days):
                money += day 
                day += 1
        return money